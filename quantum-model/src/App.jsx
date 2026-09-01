import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Float, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

// Animated data rings circulating around the quantum core
function QuantumDataRing({ radius, color, speed, count = 8 }) {
  const groupRef = useRef();

  useFrame((state) => {
    // Spin the ring data points over time
    if (groupRef.current) {
      groupRef.current.rotation.z = state.clock.getElapsedTime() * speed;
    }
  });

  return (
    <group ref={groupRef} rotation={[Math.PI / 2, 0, 0]}>
      {Array.from({ length: count }).map((_, i) => {
        const angle = (i / count) * Math.PI * 2;
        return (
          <mesh key={i} position={[Math.cos(angle) * radius, Math.sin(angle) * radius, 0]}>
            <sphereGeometry args={[0.06, 16, 16]} />
            <meshBasicMaterial color={color} toneMapped={false} />
          </mesh>
        );
      })}
      {/* Visual guidance ring path */}
      <mesh>
        <ringGeometry args={[radius - 0.01, radius + 0.01, 64]} />
        <meshBasicMaterial color={color} opacity={0.15} transparent side={THREE.DoubleSide} />
      </mesh>
    </group>
  );
}

// The structural components of the Dilution Refrigerator (The Chandelier)
function QuantumChandelier() {
  const coreRef = useRef();

  useFrame((state) => {
    // Pulse the core chip glow to simulate quantum calculation
    if (coreRef.current) {
      const glow = Math.sin(state.clock.getElapsedTime() * 4) * 0.3 + 0.7;
      coreRef.current.material.emissiveIntensity = glow;
    }
  });

  return (
    <group position={[0, 1.5, 0]}>
      {/* Top Main Flange Mounting Plate */}
      <mesh position={[0, 1, 0]}>
        <cylinderGeometry args={[2, 2, 0.15, 32]} />
        <meshStandardMaterial color="#d4af37" metalness={0.9} roughness={0.1} /> {/* Gold */}
      </mesh>

      {/* Structural Cooling Pillars (Vertical Cables) */}
      {[-0.8, 0, 0.8].map((x, idx) => (
        <group key={idx}>
          <mesh position={[x, -0.2, 0.6]}>
            <cylinderGeometry args={[0.04, 0.04, 2.2, 16]} />
            <meshStandardMaterial color="#b0b0b0" metalness={0.9} roughness={0.2} /> {/* Stainless Steel */}
          </mesh>
          <mesh position={[x, -0.2, -0.6]}>
            <cylinderGeometry args={[0.04, 0.04, 2.2, 16]} />
            <meshStandardMaterial color="#b0b0b0" metalness={0.9} roughness={0.2} />
          </mesh>
        </group>
      ))}

      {/* Mid-Stage Cryogenic Plate */}
      <mesh position={[0, 0.2, 0]}>
        <cylinderGeometry args={[1.6, 1.6, 0.1, 32]} />
        <meshStandardMaterial color="#d4af37" metalness={0.9} roughness={0.1} />
      </mesh>

      {/* Lower Mixing Chamber Stage Plate */}
      <mesh position={[0, -0.6, 0]}>
        <cylinderGeometry args={[1.2, 1.2, 0.08, 32]} />
        <meshStandardMaterial color="#d4af37" metalness={0.9} roughness={0.1} />
      </mesh>

      {/* The Quantum Qubit Core Chip Container */}
      <mesh position={[0, -1.3, 0]}>
        <cylinderGeometry args={[0.5, 0.5, 0.6, 24]} />
        <meshStandardMaterial color="#111" metalness={0.8} roughness={0.4} />
      </mesh>

      {/* Emissive Quantum Processor Matrix Core */}
      <mesh ref={coreRef} position={[0, -1.3, 0]}>
        <boxGeometry args={[0.55, 0.2, 0.55]} />
        <meshStandardMaterial 
          color="#00f3ff" 
          emissive="#00b7ff" 
          emissiveIntensity={1} 
          roughness={0.2}
        />
      </mesh>

      {/* Active Data Stream Rings circulating the Qubits */}
      <QuantumDataRing radius={0.8} color="#00f3ff" speed={1.2} count={6} />
      <QuantumDataRing radius={1.1} color="#ff00ea" speed={-0.8} count={8} />
      <QuantumDataRing radius={1.4} color="#00ff66" speed={0.5} count={5} />
    </group>
  );
}

// Main Canvas Element Wrapper
export default function QuantumComputer3D() {
  return (
    <div style={{ width: '100vw', height: '100vh', background: '#03030c' }}>
      <Canvas>
        <PerspectiveCamera makeDefault position={[0, 1, 5.5]} fov={50} />
        
        {/* Deep Space Background Lighting */}
        <ambientLight intensity={0.2} />
        <pointLight position={[10, 10, 10]} intensity={1.5} color="#fff" />
        <spotLight position={[-5, 8, -5]} intensity={2} color="#0077ff" angle={0.3} penumbra={1} />
        <spotLight position={[5, -5, 5]} intensity={1.5} color="#ff00aa" angle={0.4} />

        {/* Adds natural ambient micro-movements to the whole machine */}
        <Float speed={1.5} rotationIntensity={0.2} floatIntensity={0.3}>
          <QuantumChandelier />
        </Float>

        {/* Interactive Camera controls */}
        <OrbitControls 
          enableZoom={true} 
          maxDistance={10} 
          minDistance={3}
          autoRotate={true}
          autoRotateSpeed={0.5}
        />
      </Canvas>
    </div>
  );
}
