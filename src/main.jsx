import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const projects = [
  { title: 'Limpieza y análisis de datos', description: 'Proyecto de análisis de datos con limpieza y transformación de información mediante Python, seguido de la creación de un dashboard interactivo en Power BI.', tags: ['Python', 'Power BI', 'Análisis de datos'] },
  { title: 'Próximo análisis', description: 'Espacio preparado para presentar un dashboard de datos con indicadores, visualizaciones y conclusiones accionables.', tags: ['Power BI', 'SQL', 'Python'] },
];

function App() {
  return <main>
      <nav className="nav shell"><a className="logo" href="#inicio">Maximiliano Fernández</a></nav>
      <section className="hero shell" id="inicio"><p className="eyebrow">Data Analyst Junior · Business Intelligence</p><h1>Hola, soy <span>Maximiliano.</span></h1><p className="hero-copy">Transformo información en datos claros para entender mejor los problemas y tomar mejores decisiones.</p><div className="actions"><a className="button button-primary" href="#proyectos">Ver mis trabajos</a><a className="button button-secondary" href="#contacto">Contactarme</a></div></section>
      <section className="about shell section-grid"><div><p className="eyebrow">Sobre mí</p><h2>Curiosidad para encontrar el dato que importa.</h2></div><p className="muted">Soy Maximiliano Gabriel Fernández, tengo 33 años y estudio la Tecnicatura en Sistemas en el IFTS N°11. Estoy orientando mi perfil hacia el análisis de datos, combinando formación en Python, SQL, Power BI y Excel avanzado con más de 7 años de experiencia en ámbitos administrativos y legales, donde desarrollé una sólida capacidad para organizar información y elaborar reportes.</p></section>
      <section className="skills shell section-grid"><div><p className="eyebrow">Herramientas</p><h2>Datos que se entienden.</h2></div><p className="muted">Power BI · Excel avanzado · Python · SQL · PostgreSQL · DBeaver · Visual Studio Code · IA aplicada al análisis de datos</p></section>
      <section className="experience shell section-grid"><div><p className="eyebrow">Experiencia</p><h2>Orden, precisión y análisis.</h2></div><p className="muted">Mi paso por áreas administrativas y legales moldeó mi forma de trabajar: atención al detalle, pensamiento crítico y organización aplicados a convertir información compleja en reportes claros y accionables.</p></section>
    <section className="projects shell" id="proyectos"><div className="section-heading"><div><p className="eyebrow">Trabajos realizados</p><h2>Proyectos y análisis</h2></div><a className="text-link" href="/cv.pdf" target="_blank" rel="noreferrer">Ver CV ↗</a></div><div className="project-list">{projects.map((project, index) => <article className="project-card" key={project.title}><div className="project-number">01 / 0{index + 1}</div><h3>{project.title}</h3><p className="muted">{project.description}</p><div className="tags">{project.tags.map((tag) => <span key={tag}>{tag}</span>)}</div></article>)}</div></section>
      <section className="contact shell" id="contacto"><p className="eyebrow">Contacto</p><h2>¿Hablamos de datos?</h2><p className="muted contact-copy">Estoy abierto a oportunidades como Data Analyst Junior y proyectos relacionados con información y Business Intelligence.</p><div className="contact-links"><a href="mailto:fernandezmaximiliano255@gmail.com">fernandezmaximiliano255@gmail.com</a><a href="tel:+541162203722">+54 11 6220 3722</a><a href="https://www.linkedin.com/in/maximiliano-gabriel-fernandez-38791a2b5/" target="_blank" rel="noreferrer">LinkedIn ↗</a></div></section>
    <footer className="footer shell">© 2026 Maximiliano Fernández. Hecho con React.</footer>
  </main>;
}

createRoot(document.getElementById('root')).render(<StrictMode><App /></StrictMode>);
