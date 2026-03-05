import React, { useEffect, useRef } from 'react';
import { 
  Github, Linkedin, Mail, ExternalLink, Terminal, 
  BrainCircuit, Network, Cpu, Database, 
  Activity, Microscope, ShieldAlert, Car, Zap, Award, TrendingUp
} from 'lucide-react';

// --- ÖZEL CSS STİLLERİ ---
const CustomStyles = () => (
  <style dangerouslySetInnerHTML={{__html: `
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700;800&display=swap');
    
    body {
      font-family: 'Inter', sans-serif;
      background-color: #000000;
      color: #fafafa;
      overflow-x: hidden;
    }
    
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    .glow-text {
      text-shadow: 0 0 20px rgba(34, 197, 94, 0.6);
    }
    
    /* BOZUK NEON TABELA EFEKTİ (Broken Lamp) */
    @keyframes broken-neon {
      0%, 75% {
        opacity: 1;
        color: #22c55e;
        text-shadow: 0 0 20px rgba(34, 197, 94, 0.6), 0 0 40px rgba(34, 197, 94, 0.4);
      }
      76% { opacity: 0.3; color: #064e3b; text-shadow: none; }
      77% { opacity: 1; color: #22c55e; text-shadow: 0 0 20px rgba(34, 197, 94, 0.6); }
      78% { opacity: 0.3; color: #064e3b; text-shadow: none; }
      83% { opacity: 0.3; color: #064e3b; text-shadow: none; }
      84% { opacity: 1; color: #22c55e; text-shadow: 0 0 20px rgba(34, 197, 94, 0.6); }
      85% { opacity: 0.3; color: #064e3b; text-shadow: none; }
      86%, 100% {
        opacity: 1;
        color: #22c55e;
        text-shadow: 0 0 20px rgba(34, 197, 94, 0.6), 0 0 40px rgba(34, 197, 94, 0.4);
      }
    }
    .broken-lamp {
      animation: broken-neon 4s infinite;
      display: inline-block;
    }

    /* STANDART CAM KART */
    .glass-card {
      background: rgba(5, 10, 5, 0.6);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(34, 197, 94, 0.15);
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(34, 197, 94, 0.02);
      transition: all 0.3s ease;
    }
    .glass-card:hover {
      border-color: rgba(34, 197, 94, 0.5);
      box-shadow: 0 0 30px rgba(34, 197, 94, 0.15), inset 0 0 20px rgba(34, 197, 94, 0.05);
      transform: translateY(-2px);
    }

    /* NVIDIA ÖZEL KART (GÖZE BATAN TASARIM) */
    @keyframes pulse-nvidia {
      0% { box-shadow: 0 0 0 0 rgba(118, 185, 0, 0.4); }
      70% { box-shadow: 0 0 0 15px rgba(118, 185, 0, 0); }
      100% { box-shadow: 0 0 0 0 rgba(118, 185, 0, 0); }
    }
    .nvidia-card {
      background: linear-gradient(135deg, rgba(10, 25, 10, 0.9) 0%, rgba(0, 0, 0, 0.95) 100%);
      border: 1px solid rgba(118, 185, 0, 0.6); /* NVIDIA Yeşili */
      animation: pulse-nvidia 2.5s infinite;
      position: relative;
      overflow: hidden;
    }
    .nvidia-card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent, #76B900, transparent);
      animation: scanline 2s linear infinite;
    }
    @keyframes scanline {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }

    .scanlines {
      background: linear-gradient(
        to bottom,
        rgba(255,255,255,0),
        rgba(255,255,255,0) 50%,
        rgba(0,0,0,0.1) 50%,
        rgba(0,0,0,0.1)
      );
      background-size: 100% 4px;
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 50;
      opacity: 0.3;
    }

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #000000; }
    ::-webkit-scrollbar-thumb { background: #14532d; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #22c55e; }

    @keyframes marquee {
      0% { transform: translateX(0%); }
      100% { transform: translateX(-50%); }
    }
    .animate-marquee {
      display: inline-flex;
      white-space: nowrap;
      animation: marquee 30s linear infinite;
    }
    
    .tech-icon {
      filter: drop-shadow(0 0 8px rgba(255,255,255,0.2));
      transition: all 0.3s ease;
    }
    .tech-icon:hover {
      filter: drop-shadow(0 0 15px rgba(34, 197, 94, 0.6));
      transform: scale(1.1);
    }
  `}} />
);

// --- BİLEŞEN: ADVANCED PIXEL BLAST CANVAS ---
const AdvancedPixelBlast = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    let animationFrameId;
    let particles = [];
    let mouse = { x: -1000, y: -1000, radius: 40, isMoving: false }; 
    let mouseTimeout;

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      initParticles();
    };

    const handleMouseMove = (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      mouse.isMoving = true;
      
      clearTimeout(mouseTimeout);
      mouseTimeout = setTimeout(() => {
        mouse.isMoving = false;
      }, 100);
    };

    const handleMouseLeave = () => {
      mouse.x = -1000;
      mouse.y = -1000;
    };

    window.addEventListener('resize', handleResize);
    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mouseleave', handleMouseLeave);

    class Particle {
      constructor(x, y) {
        this.originX = x;
        this.originY = y;
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
        this.baseSize = 1.5;
        this.friction = 0.85; 
        this.spring = 0.08;   
      }

      update() {
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < mouse.radius) {
          let force = (mouse.radius - distance) / mouse.radius;
          let angle = Math.atan2(dy, dx);
          let push = mouse.isMoving ? 15 : 4; 
          this.vx -= Math.cos(angle) * force * push;
          this.vy -= Math.sin(angle) * force * push;
        }

        this.vx += (this.originX - this.x) * this.spring;
        this.vy += (this.originY - this.y) * this.spring;

        this.vx *= this.friction;
        this.vy *= this.friction;

        this.x += this.vx;
        this.y += this.vy;
      }

      draw() {
        let speed = Math.abs(this.vx) + Math.abs(this.vy);
        let currentSize = this.baseSize;
        
        ctx.beginPath();
        
        if (speed > 10) {
          ctx.fillStyle = '#ffffff';
          ctx.shadowBlur = 15;
          ctx.shadowColor = '#ffffff';
          currentSize = this.baseSize * 3;
        } else if (speed > 2) {
          ctx.fillStyle = '#22c55e';
          ctx.shadowBlur = 10;
          ctx.shadowColor = '#22c55e';
          currentSize = this.baseSize * 1.8;
        } else {
          ctx.fillStyle = '#064e3b';
          ctx.shadowBlur = 0;
        }

        ctx.rect(this.x, this.y, currentSize, currentSize);
        ctx.fill();
        ctx.shadowBlur = 0; 
      }
    }

    const initParticles = () => {
      particles = [];
      const spacing = 22; 
      for (let y = 0; y < canvas.height; y += spacing) {
        for (let x = 0; x < canvas.width; x += spacing) {
          particles.push(new Particle(x, y));
        }
      }
    };

    const animate = () => {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();
      }
      
      animationFrameId = requestAnimationFrame(animate);
    };

    handleResize();
    animate();

    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mouseleave', handleMouseLeave);
      clearTimeout(mouseTimeout);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return <canvas ref={canvasRef} className="fixed inset-0 z-0" />;
};

// --- ANA UYGULAMA BİLEŞENİ ---
export default function App() {
  const skillsList = [
    { name: "PyTorch", img: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg" },
    { name: "Python", img: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" },
    { name: "C/C++", img: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg" },
    { name: "OpenCV", img: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg" },
    { name: "Deep Learning", icon: <BrainCircuit size={28} className="text-green-500" /> },
    { name: "LLMs", icon: <Cpu size={28} className="text-purple-500" /> },
    { name: "RAG", icon: <Database size={28} className="text-blue-400" /> },
    { name: "Edge AI", icon: <Network size={28} className="text-green-400" /> },
    { name: "ONNX", icon: <Activity size={28} className="text-red-500" /> },
  ];

  return (
    <div className="relative min-h-screen selection:bg-green-500/30 selection:text-green-400">
      <CustomStyles />
      <AdvancedPixelBlast />
      <div className="scanlines"></div>

      {/* NAVBAR */}
      <nav className="fixed top-0 w-full z-50 px-6 py-6 flex justify-between items-center bg-black/60 backdrop-blur-md border-b border-green-500/10">
        <div className="flex items-center gap-3 font-mono font-bold text-xl tracking-tight text-white group cursor-pointer">
          <Terminal className="text-green-500 group-hover:rotate-12 transition-transform" size={24} />
          <span>SH4GEN<span className="text-green-500 animate-pulse">_</span></span>
        </div>
        <div className="flex gap-8 text-sm font-mono text-zinc-400">
          <a href="#work" className="hover:text-green-400 hover:drop-shadow-[0_0_8px_#22c55e] transition-all">&gt; WORK</a>
          <a href="#projects" className="hover:text-green-400 hover:drop-shadow-[0_0_8px_#22c55e] transition-all">&gt; PROJECTS</a>
          <a href="#contact" className="hover:text-white transition-all">&gt; CONTACT</a>
        </div>
      </nav>

      <main className="relative z-10 w-full max-w-5xl mx-auto px-6 pt-40 pb-32 flex flex-col gap-24">
        
        {/* HERO */}
        <section className="flex flex-col items-start pt-10">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded bg-green-500/10 border border-green-500/30 text-green-400 font-mono text-xs mb-8 shadow-[0_0_15px_rgba(34,197,94,0.1)]">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse shadow-[0_0_8px_#22c55e]"></div>
            SYSTEM.STATUS: ONLINE // RESEARCH_READY
          </div>
          
          {/* İSİM: BOZUK NEON (BROKEN LAMP) EFEKTİ TAMAMINA UYGULANDI */}
          <h1 className="font-mono text-5xl md:text-7xl lg:text-8xl font-bold tracking-tighter text-white mb-6 leading-tight uppercase">
            AŞKIN ALİ <br/>
            <span className="broken-lamp">
              BERBERGİL
            </span>
          </h1>
          
          <div className="flex flex-col md:flex-row gap-8 items-start md:items-center w-full justify-between mt-4">
            <p className="text-zinc-400 text-lg font-light max-w-xl leading-relaxed border-l-2 border-green-500/30 pl-4">
              AI Engineer & Software Engineering student specializing in low-latency computer vision, deep learning pipelines, and autonomous perception.
            </p>
            
            <div className="flex gap-4 shrink-0">
              <a href="https://github.com/sh4gen" target="_blank" rel="noreferrer" className="p-3 bg-black/50 border border-green-500/30 hover:bg-green-500/10 hover:border-green-400 hover:text-green-400 rounded transition-all text-zinc-400 group relative">
                <Github size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
              <a href="https://linkedin.com/in/askinaliberbergil" target="_blank" rel="noreferrer" className="p-3 bg-black/50 border border-green-500/30 hover:bg-green-500/10 hover:border-green-400 hover:text-green-400 rounded transition-all text-zinc-400 group relative">
                <Linkedin size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
              <a href="mailto:askinaliberbergil@gmail.com" className="p-3 bg-black/50 border border-green-500/30 hover:bg-green-500/10 hover:border-green-400 hover:text-green-400 rounded transition-all text-zinc-400 group relative">
                <Mail size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
            </div>
          </div>
        </section>

        {/* YETENEKLER */}
        <section className="w-full overflow-hidden py-10 border-y border-green-500/20 bg-gradient-to-r from-black via-green-950/20 to-black backdrop-blur-sm -mx-6 px-6 box-content">
          <div className="animate-marquee flex gap-16 items-center">
            {[...skillsList, ...skillsList, ...skillsList, ...skillsList].map((skill, i) => (
              <div key={i} className="flex items-center gap-3 group cursor-crosshair">
                {skill.img ? (
                  <img src={skill.img} alt={skill.name} className="w-8 h-8 tech-icon" />
                ) : (
                  <div className="tech-icon">{skill.icon}</div>
                )}
                <span className="font-mono text-2xl font-bold text-zinc-700 group-hover:text-white transition-colors duration-300 uppercase tracking-wider">
                  {skill.name}
                </span>
              </div>
            ))}
          </div>
        </section>

        {/* DENEYİM */}
        <section id="work" className="flex flex-col gap-8 relative">
          <div className="flex items-center gap-4 mb-4">
            <BrainCircuit className="text-green-500 glow-text" size={32} />
            <h2 className="font-mono text-3xl font-bold text-white">EXPERIENCE<span className="text-green-500 animate-pulse">_</span></h2>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="glass-card p-8 rounded-xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-30 group-hover:scale-110 transition-all duration-500">
                <Activity size={120} className="text-green-500" />
              </div>
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-white mb-1">AKGÜN</h3>
                    <div className="font-mono text-green-400 text-sm flex items-center gap-2">
                      <Terminal size={14}/> AI Engineer Intern
                    </div>
                  </div>
                  <span className="text-zinc-400 font-mono text-xs px-2 py-1 border border-green-500/20 rounded bg-green-500/5">Jul '25 - Jan '26</span>
                </div>
                <p className="text-zinc-400 text-sm leading-relaxed mt-4">
                  Developed Cajal's Brain Tumor Segmentation modular medical imaging pipeline for MRI-based tumor analysis. Integrated local LLMs using RAG pipelines to generate structured quality-control reports. Optimized CPU inference with <span className="text-green-400 font-bold tracking-wide">ONNX & OpenVINO</span> for hospital hardware.
                </p>
              </div>
            </div>

            <div className="glass-card p-8 rounded-xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-30 group-hover:scale-110 transition-all duration-500">
                <Microscope size={120} className="text-green-500" />
              </div>
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-white mb-1">MİA TEKNOLOJİ</h3>
                    <div className="font-mono text-green-400 text-sm flex items-center gap-2">
                      <Terminal size={14}/> AI Engineer Intern
                    </div>
                  </div>
                  <span className="text-zinc-400 font-mono text-xs px-2 py-1 border border-green-500/20 rounded bg-green-500/5">Aug '24 - Sep '24</span>
                </div>
                <p className="text-zinc-400 text-sm leading-relaxed mt-4">
                  Developed deep learning models for <span className="text-white">dental image analysis</span> and gum inflammation detection. Built ARIMA-based forecasting models for medication usage trends.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* PROJELER & ARAŞTIRMA */}
        <section id="projects" className="flex flex-col gap-8">
          <div className="flex items-center gap-4 mb-4">
            <Cpu className="text-green-500 glow-text" size={32} />
            <h2 className="font-mono text-3xl font-bold text-white">RESEARCH_&_PROJECTS<span className="text-green-500 animate-pulse">_</span></h2>
          </div>

          <div className="flex flex-col gap-8">
            {/* NVIDIA PROJESİ (VIP KART TASARIMI) */}
            <div className="nvidia-card p-8 md:p-10 rounded-xl flex flex-col md:flex-row gap-8 items-start group">
              <div className="absolute -bottom-10 -right-10 opacity-10 group-hover:opacity-30 transition-opacity duration-500 pointer-events-none">
                <ShieldAlert size={240} color="#76B900" />
              </div>
              
              <div className="w-full md:w-1/3 relative z-10 flex flex-col items-start">
                <div className="inline-flex items-center gap-2 px-4 py-2 bg-[#76B900]/20 text-[#76B900] font-mono text-sm font-bold border border-[#76B900]/50 rounded mb-4 shadow-[0_0_15px_rgba(118,185,0,0.4)]">
                  <Award size={18} />
                  NVIDIA GRANT
                </div>
                <h3 className="text-2xl font-bold text-white mb-4 leading-tight group-hover:text-[#76B900] transition-colors">
                  Synthetic Data Enhanced Multi-Camera Intruder Detection
                </h3>
                
                {/* DONANIM VURGUSU */}
                <div className="mt-2 mb-6 inline-flex items-center gap-2 px-3 py-2 bg-black/80 border border-green-400/50 rounded-lg text-green-300 font-mono text-xs shadow-[0_0_10px_rgba(34,197,94,0.2)]">
                  <Zap size={14} className="text-yellow-400 animate-pulse" />
                  Powered by 4x RTX Pro 6000 GPUs
                </div>

                <div className="flex flex-wrap gap-2">
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-[#76B900]/30">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg" className="w-3.5 h-3.5" alt="PyTorch"/> PyTorch
                  </span>
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-[#76B900]/30">
                    <Network size={14} className="text-[#76B900]"/> Edge AI
                  </span>
                </div>
              </div>

              <div className="w-full md:w-2/3 relative z-10">
                <p className="text-zinc-300 text-[15px] leading-relaxed mb-4">
                  Received highly prestigious <strong className="text-white">NVIDIA Academic Grant</strong> supporting person re-identification research. Developed a complex multi-camera intruder tracking pipeline integrating person detection and re-identification, training custom models for cross-camera identity matching.
                </p>
                <p className="text-zinc-300 text-[15px] leading-relaxed">
                  Optimized computer vision models for <strong className="text-[#76B900]">low-latency deployment on NVIDIA Jetson edge devices</strong>. Trained and evaluated models using synthetic and real-world datasets. Submitted a research manuscript based on system development (under review).
                </p>
              </div>
            </div>

            {/* BIST STOCK SELECTION PROJESİ */}
            <div className="glass-card p-8 rounded-xl flex flex-col md:flex-row gap-8 items-start group relative overflow-hidden">
               <div className="absolute -bottom-10 -right-10 opacity-5 group-hover:opacity-20 transition-opacity duration-500 pointer-events-none">
                <TrendingUp size={200} className="text-blue-500" />
              </div>

               <div className="w-full md:w-1/3 relative z-10">
                <span className="inline-block px-3 py-1.5 bg-blue-500/10 text-blue-400 font-mono text-xs font-bold border border-blue-500/30 rounded mb-4 shadow-[0_0_10px_rgba(59,130,246,0.2)]">
                  ALGORITHMIC TRADING
                </span>
                <h3 className="text-xl font-bold text-white mb-4 group-hover:text-blue-400 transition-colors">BIST Weekly ML Stock Selection System</h3>
                <div className="flex flex-wrap gap-2 mb-4">
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-zinc-700">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" className="w-3.5 h-3.5" alt="Python"/> Python
                  </span>
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-zinc-700">
                    <Database size={14} className="text-blue-400"/> Data Scrape
                  </span>
                </div>
                {/* GITHUB REPO BUTONU */}
                <a href="https://github.com/sh4gen/BIST-Weekly-ML-Stock-Selection-System" target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 text-xs font-mono text-zinc-400 hover:text-white border border-zinc-700 hover:border-zinc-500 bg-black/50 px-3 py-2 rounded transition-all group-hover:border-blue-500/50">
                   <Github size={14} /> View Repository <ExternalLink size={12}/>
                </a>
              </div>
              <div className="w-full md:w-2/3 relative z-10">
                <p className="text-zinc-400 text-sm leading-relaxed mt-2">
                  Developed an end-to-end machine learning pipeline designed to analyze and select promising stocks on the <strong className="text-white">Borsa Istanbul (BIST)</strong> on a weekly basis. 
                  <br/><br/>
                  The system automates financial data fetching, performs advanced feature engineering, and utilizes predictive modeling algorithms to identify high-potential market opportunities for algorithmic trading strategies.
                </p>
              </div>
            </div>

            {/* TEKNOFEST PROJESİ */}
            <div className="glass-card p-8 rounded-xl flex flex-col md:flex-row gap-8 items-start group relative overflow-hidden">
               <div className="absolute -bottom-10 -right-10 opacity-5 group-hover:opacity-20 transition-opacity duration-500 pointer-events-none">
                <Car size={200} className="text-white" />
              </div>
              
               <div className="w-full md:w-1/3 relative z-10">
                <span className="inline-block px-3 py-1.5 bg-red-500/10 text-red-400 font-mono text-xs font-bold border border-red-500/30 rounded mb-4 shadow-[0_0_10px_rgba(239,68,68,0.2)]">
                  TEKNOFEST TÜBİTAK
                </span>
                <h3 className="text-xl font-bold text-white mb-4 group-hover:text-red-400 transition-colors">Robotaksi Autonomous Vehicle Perception System</h3>
                <div className="flex flex-wrap gap-2">
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-zinc-700">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" className="w-3.5 h-3.5" alt="Python"/> Python
                  </span>
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-zinc-700">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg" className="w-3.5 h-3.5" alt="OpenCV"/> OpenCV
                  </span>
                  <span className="flex items-center gap-1.5 text-xs font-mono text-zinc-300 bg-black/60 px-2 py-1.5 rounded border border-zinc-700">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/unity/unity-original.svg" className="w-3.5 h-3.5 bg-white rounded-sm" alt="Unity"/> Unity
                  </span>
                </div>
              </div>
              <div className="w-full md:w-2/3 relative z-10">
                <p className="text-zinc-400 text-sm leading-relaxed">
                  <strong className="text-white">AI Team Lead.</strong> Led the AI team responsible for autonomous driving perception systems. Implemented <span className="text-green-400">lane detection and traffic sign recognition pipelines</span>. Built Unity-based simulation environments to test and validate perception models safely before real-world deployment.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* EĞİTİM & LİDERLİK */}
        <section className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-12 border-t border-green-500/20">
          <div className="glass-card p-8 rounded-xl border-l-4 border-l-green-500">
            <div className="font-mono text-green-500/50 text-xs mb-4 flex items-center gap-2">
              <Terminal size={14} /> // EDUCATION
            </div>
            <h3 className="text-xl font-bold text-white mb-1">Atılım University</h3>
            <p className="text-green-400 font-mono text-sm mb-6">B.Sc. in Software Engineering</p>
            <div className="flex justify-between items-center text-sm text-zinc-400 pb-3 border-b border-green-500/10 mb-3">
              <span>Timeline</span>
              <span className="font-mono bg-green-500/10 px-2 py-0.5 rounded text-green-400">2022 - 2026</span>
            </div>
            <div className="flex justify-between items-center text-sm text-zinc-400">
              <span>GPA</span>
              <span className="font-mono text-white glow-text">2.76 / 4.00</span>
            </div>
          </div>
          
          <div className="glass-card p-8 rounded-xl border-l-4 border-l-blue-500">
            <div className="font-mono text-zinc-500 text-xs mb-4 flex items-center gap-2">
              <Terminal size={14} /> // LEADERSHIP
            </div>
            <h3 className="text-xl font-bold text-white mb-1">Atılım AI Club</h3>
            <p className="text-blue-400 font-mono text-sm mb-4">Board Member</p>
            <p className="text-zinc-400 text-sm leading-relaxed">
              Delivered Machine Learning lectures & workshops. Organized hands-on training sessions and led the development of real-time computer vision projects for the university community.
            </p>
          </div>
        </section>

      </main>

      {/* FOOTER */}
      <footer id="contact" className="relative z-10 w-full py-20 border-t border-green-500/30 bg-black/90 backdrop-blur-xl flex flex-col items-center justify-center text-center">
        <Network size={40} className="text-green-500 mb-6 drop-shadow-[0_0_15px_rgba(34,197,94,0.6)] animate-pulse" />
        <h2 className="font-mono text-3xl md:text-4xl font-bold text-white mb-6">INITIATE_CONNECTION</h2>
        <a href="mailto:askinaliberbergil@gmail.com" className="inline-flex items-center gap-3 font-mono text-green-400 hover:text-white bg-green-500/10 hover:bg-green-500/30 border border-green-500/50 px-8 py-4 rounded transition-all group shadow-[0_0_20px_rgba(34,197,94,0.1)] hover:shadow-[0_0_30px_rgba(34,197,94,0.3)]">
          <Terminal size={18} className="text-green-500 group-hover:text-white transition-colors" />
          askinaliberbergil@gmail.com
          <ExternalLink size={18} className="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
        </a>
        <p className="mt-16 font-mono text-zinc-600 text-xs tracking-widest uppercase">
          [ SYSTEM.EXIT(0) ] © {new Date().getFullYear()} AŞKIN ALİ BERBERGİL
        </p>
      </footer>
    </div>
  );
}