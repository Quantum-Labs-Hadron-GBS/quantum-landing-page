-- Hadron Quantum Publisher (HQ Studio) - Enterprise Schema

-- 1. Lookup Tables
CREATE TABLE public.statuses (
    id smallint PRIMARY KEY,
    name text NOT NULL UNIQUE
);

INSERT INTO public.statuses (id, name) VALUES
    (1, 'Draft'),
    (2, 'Review'),
    (3, 'Published'),
    (4, 'Archived');

CREATE TABLE public.document_types (
    id text PRIMARY KEY,
    name text NOT NULL
);

INSERT INTO public.document_types (id, name) VALUES
    ('BLOG', 'Blog Post'),
    ('RESEARCH', 'Research Paper'),
    ('WHITEPAPER', 'Whitepaper'),
    ('CASE_STUDY', 'Case Study'),
    ('NEWS', 'News & Updates'),
    ('EVENT', 'Event'),
    ('DOCUMENTATION', 'Documentation');

-- 2. Documents Table
CREATE TABLE public.documents (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    type_id text REFERENCES public.document_types(id) NOT NULL DEFAULT 'BLOG',
    status_id smallint REFERENCES public.statuses(id) NOT NULL DEFAULT 1,
    title text NOT NULL,
    slug text UNIQUE NOT NULL,
    markdown text,
    html text,
    excerpt text,
    cover_image text,
    reading_time text,
    author_id uuid REFERENCES auth.users(id),
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    published_at timestamp with time zone,
    seo_metadata jsonb DEFAULT '{}'::jsonb
);

-- Enable Full Text Search on Documents
ALTER TABLE public.documents
ADD COLUMN search_vector tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', coalesce(title, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(markdown, '')), 'B')
) STORED;

CREATE INDEX documents_search_idx ON public.documents USING GIN (search_vector);

-- 3. Document Versions (For Version History)
CREATE TABLE public.document_versions (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id uuid REFERENCES public.documents(id) ON DELETE CASCADE NOT NULL,
    markdown text,
    html text,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);

-- 4. Triggers for Version History & Updated At
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_documents_updated_at
    BEFORE UPDATE ON public.documents
    FOR EACH ROW
    EXECUTE FUNCTION public.handle_updated_at();

CREATE OR REPLACE FUNCTION public.create_document_version()
RETURNS TRIGGER AS $$
BEGIN
    -- Only create a version if markdown or html actually changed
    IF (OLD.markdown IS DISTINCT FROM NEW.markdown) OR (OLD.html IS DISTINCT FROM NEW.html) THEN
        INSERT INTO public.document_versions (document_id, markdown, html)
        VALUES (NEW.id, NEW.markdown, NEW.html);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER create_version_on_update
    AFTER UPDATE ON public.documents
    FOR EACH ROW
    EXECUTE FUNCTION public.create_document_version();

-- 5. Row Level Security (RLS)
ALTER TABLE public.documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.document_versions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.statuses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.document_types ENABLE ROW LEVEL SECURITY;

-- Allow public read access to Published documents (status 3)
CREATE POLICY "Public can read published documents"
ON public.documents FOR SELECT
TO public
USING (status_id = 3);

-- Allow authenticated users (Admins) to do everything
CREATE POLICY "Authenticated users can manage documents"
ON public.documents FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- Allow authenticated users to view/restore versions
CREATE POLICY "Authenticated users can manage versions"
ON public.document_versions FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- Lookup tables are readable by everyone
CREATE POLICY "Public read statuses" ON public.statuses FOR SELECT USING (true);
CREATE POLICY "Public read document types" ON public.document_types FOR SELECT USING (true);

-- Create Storage Bucket for Media (Note: bucket creation might need to be run as postgres superuser, but RLS policies can be run here)
-- INSERT INTO storage.buckets (id, name, public) VALUES ('media', 'media', true);

CREATE POLICY "Authenticated users can upload media"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'media');

CREATE POLICY "Public can view media"
ON storage.objects FOR SELECT
TO public
USING (bucket_id = 'media');

-- 6. Role Permissions (Fix for "permission denied" errors)
GRANT ALL ON TABLE public.statuses TO anon, authenticated, service_role;
GRANT ALL ON TABLE public.document_types TO anon, authenticated, service_role;
GRANT ALL ON TABLE public.documents TO anon, authenticated, service_role;
GRANT ALL ON TABLE public.document_versions TO anon, authenticated, service_role;
