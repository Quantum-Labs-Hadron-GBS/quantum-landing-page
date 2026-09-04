import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Extract the hero-news-card block
    news_card_regex = re.compile(r'<a id="hero-news-card".*?</a>', re.DOTALL)
    news_card_match = news_card_regex.search(html)
    if not news_card_match:
        print("News card not found!")
        return
    news_card_html = news_card_match.group(0)

    # Make it pointer-events-auto so it's clickable inside the pointer-events-none tracking layer
    # Also remove any hidden classes if it needs to be visible always to cover the watermark
    news_card_html = news_card_html.replace('block"', 'block pointer-events-auto"')

    # 2. Remove it from the Right Column in the grid
    # The grid right column looks like:
    # <div class="hidden lg:flex flex-col justify-end h-full">
    #     <a id="hero-news-card" ...>...</a>
    # </div>
    right_col_regex = re.compile(r'<!-- Right Column -->\s*<div class="hidden lg:flex flex-col justify-end h-full">\s*<a id="hero-news-card".*?</a>\s*</div>', re.DOTALL)
    html = right_col_regex.sub('<!-- Right Column (Moved to Tracking Layer) -->\n                        <div class="hidden lg:flex flex-col justify-end h-full"></div>', html)

    # 3. Insert the Tracking Layer right after the <video> tag
    tracking_layer = f'''
                <!-- Video Tracking Layer for Watermark -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none"
                     style="width: max(100vw, 177.77vh); height: max(100vh, 56.25vw); z-index: 15;">
                     <!-- Positioned over the watermark (bottom right area) -->
                     <div class="absolute" style="bottom: 12%; right: 12%; width: 22%; min-width: 300px;">
                         {news_card_html}
                     </div>
                </div>
'''
    html = html.replace('</video>', '</video>\n' + tracking_layer)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("News box updated successfully.")

if __name__ == '__main__':
    update_index()
