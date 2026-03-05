const { useEffect, useRef } = React;

// Simple icon placeholders (avoid external icon packages for static deploy)
const Icon = ({children, size=20, className=''}) => (
  <span className={className} style={{fontSize:size, display:'inline-flex', alignItems:'center'}}>{children}</span>
);
const Github = (p) => <Icon {...p}>🐱</Icon>;
const Linkedin = (p) => <Icon {...p}>🔗</Icon>;
const Mail = (p) => <Icon {...p}>✉️</Icon>;
const Terminal = (p) => <Icon {...p}>⌁</Icon>;
const BrainCircuit = (p) => <Icon {...p}>🧠</Icon>;
const Network = (p) => <Icon {...p}>🌐</Icon>;
const Cpu = (p) => <Icon {...p}>💻</Icon>;
const Database = (p) => <Icon {...p}>🗄️</Icon>;
const Activity = (p) => <Icon {...p}>⚡</Icon>;
const Microscope = (p) => <Icon {...p}>🔬</Icon>;

// Advanced pixel blast canvas (kept from original code)
function AdvancedPixelBlast(){
  const canvasRef = useRef(null);

  useEffect(()=>{
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    let animationFrameId;
    let particles = [];
    let mouse = { x:-1000, y:-1000, radius:40, isMoving:false };
    let mouseTimeout;

    const handleResize = ()=>{
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      initParticles();
    };

    const handleMouseMove = (e)=>{
      mouse.x = e.clientX; mouse.y = e.clientY; mouse.isMoving = true;
      clearTimeout(mouseTimeout);
      mouseTimeout = setTimeout(()=>{ mouse.isMoving = false; }, 100);
    };

    const handleMouseLeave = ()=>{ mouse.x = -1000; mouse.y = -1000; };

    window.addEventListener('resize', handleResize);
    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mouseleave', handleMouseLeave);

    class Particle {
      constructor(x,y){ this.originX=x; this.originY=y; this.x=x; this.y=y; this.vx=0; this.vy=0; this.baseSize=1.5; this.friction=0.85; this.spring=0.08; }
      update(){
        let dx = mouse.x - this.x; let dy = mouse.y - this.y; let distance = Math.sqrt(dx*dx + dy*dy);
        if(distance < mouse.radius){ let force = (mouse.radius - distance)/mouse.radius; let angle = Math.atan2(dy,dx); let push = mouse.isMoving ? 15 : 4; this.vx -= Math.cos(angle)*force*push; this.vy -= Math.sin(angle)*force*push; }
        this.vx += (this.originX - this.x) * this.spring; this.vy += (this.originY - this.y) * this.spring;
        this.vx *= this.friction; this.vy *= this.friction; this.x += this.vx; this.y += this.vy;
      }
      draw(){
        let speed = Math.abs(this.vx) + Math.abs(this.vy); let currentSize = this.baseSize;
        ctx.beginPath();
        if(speed > 10){ ctx.fillStyle = '#ffffff'; ctx.shadowBlur = 15; ctx.shadowColor = '#ffffff'; currentSize = this.baseSize * 3; }
        else if(speed > 2){ ctx.fillStyle = '#22c55e'; ctx.shadowBlur = 10; ctx.shadowColor = '#22c55e'; currentSize = this.baseSize * 1.8; }
        else { ctx.fillStyle = '#064e3b'; ctx.shadowBlur = 0; }
        ctx.rect(this.x, this.y, currentSize, currentSize); ctx.fill(); ctx.shadowBlur = 0;
      }
    }

    const initParticles = ()=>{
      particles = []; const spacing = 22;
      for(let y=0;y<canvas.height;y+=spacing){ for(let x=0;x<canvas.width;x+=spacing){ particles.push(new Particle(x,y)); } }
    };

    const animate = ()=>{
      ctx.fillStyle = 'rgba(0,0,0,0.3)'; ctx.fillRect(0,0,canvas.width,canvas.height);
      for(let i=0;i<particles.length;i++){ particles[i].update(); particles[i].draw(); }
      animationFrameId = requestAnimationFrame(animate);
    };

    handleResize(); animate();

    return ()=>{ window.removeEventListener('resize', handleResize); window.removeEventListener('mousemove', handleMouseMove); window.removeEventListener('mouseleave', handleMouseLeave); clearTimeout(mouseTimeout); cancelAnimationFrame(animationFrameId); };
  }, []);

  return <canvas ref={canvasRef} className="fixed inset-0 z-0" />;
}

function App(){
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
      <AdvancedPixelBlast />
      <div className="scanlines"></div>

      <nav className="fixed top-0 w-full z-50 px-6 py-6 flex justify-between items-center bg-black/60 backdrop-blur-md border-b border-green-500/10">
        <div className="flex items-center gap-3 font-mono font-bold text-xl tracking-tight text-white group cursor-pointer">
          <Terminal className="text-green-500 group-hover:rotate-12 transition-transform" size={24} />
          <span>SH4GEN<span className="text-green-500 animate-pulse">_</span></span>
        </div>
        <div className="flex gap-8 text-sm font-mono text-zinc-400">
          <a href="#work" className="hover:text-green-400">&gt; WORK</a>
          <a href="#projects" className="hover:text-green-400">&gt; PROJECTS</a>
          <a href="#contact" className="hover:text-white">&gt; CONTACT</a>
        </div>
      </nav>

      <main className="relative z-10 w-full max-w-5xl mx-auto px-6 pt-40 pb-32 flex flex-col gap-24">
        <section className="flex flex-col items-start pt-10">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded bg-green-500/10 border border-green-500/30 text-green-400 font-mono text-xs mb-8 shadow-[0_0_15px_rgba(34,197,94,0.1)]">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse shadow-[0_0_8px_#22c55e]"></div>
            SYSTEM.STATUS: ONLINE // RESEARCH_READY
          </div>

          <h1 className="font-mono text-5xl md:text-7xl lg:text-8xl font-bold tracking-tighter text-white mb-6 leading-tight uppercase">
            AŞKIN ALİ <br/>
            <span className="broken-lamp">BERBERGİL</span>
          </h1>

          <div className="flex flex-col md:flex-row gap-8 items-start md:items-center w-full justify-between mt-4">
            <p className="text-zinc-400 text-lg font-light max-w-xl leading-relaxed border-l-2 border-green-500/30 pl-4">
              AI Engineer & Software Engineering student specializing in low-latency computer vision, deep learning pipelines, and autonomous perception.
            </p>

            <div className="flex gap-4 shrink-0">
              <a href="https://github.com/sh4gen" target="_blank" rel="noreferrer" className="p-3 bg-black/50 border border-green-500/30 rounded transition-all text-zinc-400 group relative">
                <Github size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
              <a href="https://linkedin.com/in/askinaliberbergil" target="_blank" rel="noreferrer" className="p-3 bg-black/50 border border-green-500/30 rounded transition-all text-zinc-400 group relative">
                <Linkedin size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
              <a href="mailto:askinaliberbergil@gmail.com" className="p-3 bg-black/50 border border-green-500/30 rounded transition-all text-zinc-400 group relative">
                <Mail size={22} className="group-hover:drop-shadow-[0_0_8px_#22c55e] relative z-10" />
              </a>
            </div>
          </div>
        </section>

        <section className="w-full overflow-hidden py-10 border-y border-green-500/20 bg-gradient-to-r from-black via-green-950/20 to-black backdrop-blur-sm -mx-6 px-6 box-content">
          <div className="animate-marquee flex gap-16 items-center">
            {[...skillsList, ...skillsList].map((skill, i)=> (
              <div key={i} className="flex items-center gap-3 group cursor-crosshair">
                {skill.img ? (<img src={skill.img} alt={skill.name} className="w-8 h-8 tech-icon" />) : (<div className="tech-icon">{skill.icon}</div>)}
                <span className="font-mono text-2xl font-bold text-zinc-700 group-hover:text-white transition-colors duration-300 uppercase tracking-wider">{skill.name}</span>
              </div>
            ))}
          </div>
        </section>

        <section id="work" className="flex flex-col gap-8 relative">
          <div className="flex items-center gap-4 mb-4">
            <BrainCircuit className="text-green-500 glow-text" size={32} />
            <h2 className="font-mono text-3xl font-bold text-white">EXPERIENCE<span className="text-green-500 animate-pulse">_</span></h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="glass-card p-8 rounded-xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-30 transition-all duration-500">
                <Activity size={120} className="text-green-500" />
              </div>
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-white mb-1">AKGÜN</h3>
                    <div className="font-mono text-green-400 text-sm flex items-center gap-2"><Terminal size={14}/> AI Engineer Intern</div>
                  </div>
                  <span className="text-zinc-400 font-mono text-xs px-2 py-1 border border-green-500/20 rounded bg-green-500/5">Jul '25 - Jan '26</span>
                </div>
                <p className="text-zinc-400 text-sm leading-relaxed mt-4">Developed Cajal's Brain Tumor Segmentation modular medical imaging pipeline for MRI-based tumor analysis. Integrated local LLMs using RAG pipelines to generate structured quality-control reports. Optimized CPU inference with <span className="text-green-400 font-bold tracking-wide">ONNX & OpenVINO</span> for hospital hardware.</p>
              </div>
            </div>

            <div className="glass-card p-8 rounded-xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-30 transition-all duration-500">
                <Microscope size={120} className="text-green-500" />
              </div>
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-white mb-1">MİA TEKNOLOJİ</h3>
                    <div className="font-mono text-green-400 text-sm flex items-center gap-2"><Terminal size={14}/> AI Engineer Intern</div>
                  </div>
                  <span className="text-zinc-400 font-mono text-xs px-2 py-1 border border-green-500/20 rounded bg-green-500/5">Aug '24 - Sep '24</span>
                </div>
                <p className="text-zinc-400 text-sm leading-relaxed mt-4">Worked on computer vision and inference pipelines for embedded systems.</p>
              </div>
            </div>
          </div>
        </section>

        {/* projects section added for single-page navigation */}
        <section id="projects" className="flex flex-col gap-8 relative">
          <div className="flex items-center gap-4 mb-4">
            <Network className="text-green-500 glow-text" size={32} />
            <h2 className="font-mono text-3xl font-bold text-white">PROJECTS<span className="text-green-500 animate-pulse">_</span></h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* example project card */}
            <div className="glass-card p-8 rounded-xl relative overflow-hidden group">
              <h3 className="text-2xl font-bold text-white mb-2">Example Project</h3>
              <p className="text-zinc-400 text-sm leading-relaxed">A brief description of a project. Replace with real content or links.</p>
              <a href="#" className="mt-4 inline-block text-green-400 font-mono text-sm">View on GitHub →</a>
            </div>
          </div>
        </section>

        <section id="contact" className="flex flex-col gap-8 relative">
          <div className="flex items-center gap-4 mb-4">
            <Mail className="text-green-500 glow-text" size={32} />
            <h2 className="font-mono text-3xl font-bold text-white">CONTACT<span className="text-green-500 animate-pulse">_</span></h2>
          </div>

          <div className="text-zinc-400">
            <p>If you'd like to get in touch, feel free to send an email to <a href="mailto:askinaliberbergil@gmail.com" className="text-green-400 underline">askinaliberbergil@gmail.com</a> or connect via LinkedIn.</p>
          </div>
        </section>
      </main>
    </div>
  );
}

const root = document.getElementById('root');
ReactDOM.createRoot(root).render(<App />);
