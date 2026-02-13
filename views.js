/**
 * views.js
 * Contains all the HTML components for the Single Page Application (SPA).
 */
export const views = {
    home: `
    <section id="home" class="hero">
      <div class="grid-overlay"></div>

      <div class="container hero-container">
        <div class="hero-content">
          <div class="badge-container">
            <span class="badge-hire">AVAILABLE FOR HIRE</span>
          </div>

          <h1 class="hero-name">Denis <span class="text-blue">Syengo</span></h1>
          <h2 class="hero-role">
            Full-Stack, DevOps & <br />
            Cybersecurity Specialist
          </h2>

          <p class="hero-description">
            Software Engineer and Cybersecurity Specialist with full-stack
            expertise in building secure, scalable, and resilient systems.
            Experienced in backend architecture, cross-platform applications,
            and integrating security throughout the development lifecycle.
            DevOps-inclined, with a focus on automation, reliability, and
            performance. Passionate about leveraging AI to enhance efficiency,
            security, and intelligent digital solutions.
          </p>

          <div class="hero-actions">
            <a href="#projects" class="btn btn-primary">View Projects</a>
            <a href="assets/cv.pdf" class="btn btn-outline" download>
              <i class="bi bi-download me-2"></i> Download CV
            </a>
          </div>

          <div class="hero-socials">
            <a href="#" class="social-box"><i class="bi bi-github"></i></a>
            <a href="#" class="social-box"><i class="bi bi-linkedin"></i></a>
            <a href="#" class="social-box"><i class="bi bi-twitter-x"></i></a>
            <a href="#" class="social-box"><i class="bi bi-envelope"></i></a>
          </div>
        </div>

        <div class="hero-image-area">
          <div class="image-glowing-wrapper">
            <div class="main-image-container">
              <img
                src="assets/denis-profile.jpeg"
                alt="Denis Syengo"
                class="profile-img"
              />
            </div>
            <div class="status-badge">
              <span class="status-dot"></span> Open to Work
            </div>
          </div>
        </div>
      </div>
    </section>
    `,

    about: `
    <section id="about" class="about-section">
      <div class="container">
        <div class="section-header">
          <span class="badge-pill">About Me</span>
          <h2 class="section-title">Security-First Problem Solver</h2>
        </div>

        <div class="about-main-grid">
          <div class="bio-column">
            <div class="bio-card">
              <p class="bio-lead">
                I'm a Full-Stack & DevOps engineer with a passion for building
                secure, high-performance applications.
              </p>
              <p class="bio-text">
                My approach combines deep technical expertise in both
                development and cybersecurity, allowing me to identify
                vulnerabilities early and implement security best practices from
                the ground up.
              </p>
              <p class="bio-text">
                With a disciplined and strategic mindset, I specialize in
                designing scalable microservices, performing in-depth security
                assessments, and optimizing cloud infrastructure. I focus on
                solving complex, high-impact challenges through resilient
                architecture, clean system design, and security-first
                engineering.
              </p>
            </div>
          </div>

          <div class="skills-column">
            <div class="skill-item">
              <div class="skill-label">
                <span
                  ><i class="bi bi-code-slash"></i> Frontend Development</span
                >
                <span class="skill-val">95%</span>
              </div>
              <div class="progress-bg">
                <div
                  class="progress-fill"
                  style="width: 95%; background: #007bff"
                ></div>
              </div>
            </div>

            <div class="skill-item">
              <div class="skill-label">
                <span
                  ><i class="bi bi-hdd-network"></i> Backend Architecture</span
                >
                <span class="skill-val">92%</span>
              </div>
              <div class="progress-bg">
                <div
                  class="progress-fill"
                  style="width: 92%; background: #6f42c1"
                ></div>
              </div>
            </div>

            <div class="skill-item">
              <div class="skill-label">
                <span><i class="bi bi-shield-check"></i> Cybersecurity</span>
                <span class="skill-val">90%</span>
              </div>
              <div class="progress-bg">
                <div
                  class="progress-fill"
                  style="width: 90%; background: #20c997"
                ></div>
              </div>
            </div>

            <div class="skill-item">
              <div class="skill-label">
                <span
                  ><i class="bi bi-shield-check"></i> Cloud infrastructure</span
                >
                <span class="skill-val">70%</span>
              </div>
              <div class="progress-bg">
                <div
                  class="progress-fill"
                  style="width: 70%; background: #d63384"
                ></div>
              </div>
            </div>

            <div class="skill-item">
              <div class="skill-label">
                <span><i class="bi bi-shield-check"></i> DevOps & CI Cd</span>
                <span class="skill-val">89%</span>
              </div>
              <div class="progress-bg">
                <div
                  class="progress-fill"
                  style="width: 87%; background: #0dcaf0"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <div class="stack-section">
          <h3 class="stack-title">Technology Stack</h3>
          <div class="stack-grid">
            <div class="stack-card">
              <h4>Frontend</h4>
              <div class="pill-container">
                <span class="stack-pill">React</span>
                <span class="stack-pill">Angular</span>
                <span class="stack-pill">TypeScript</span>
                <span class="stack-pill">Tailwind CSS</span>
                <span class="stack-pill">Bootsrap</span>
              </div>
            </div>
            <div class="stack-card">
              <h4>Backend</h4>
              <div class="pill-container">
                <span class="stack-pill">Node.js</span>
                <span class="stack-pill">Python</span>
                <span class="stack-pill">Django</span>
                <span class="stack-pill">Express</span>
                <span class="stack-pill">PostgreSQL</span>
              </div>
            </div>
            <div class="stack-card">
              <h4>DevOps</h4>
              <div class="pill-container">
                <span class="stack-pill">Docker</span>
                <span class="stack-pill">Kubernetes</span>
                <span class="stack-pill">AWS</span>
                <span class="stack-pill">Azure</span>
                <span class="stack-pill">Terraform</span>
              </div>
            <!-- </div>
            <div class="stack-card">
              <h4>Security</h4>
              <div class="pill-container">
                <span class="stack-pill">OWASP</span>
                <span class="stack-pill">Pen-Testing</span>
                <span class="stack-pill">Encryption</span>
                <span class="stack-pill">OAuth</span>
                <span class="stack-pill">JWT</span>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </section>
    `,

    projects: `
    <section id="projects" class="projects-section">
    <div class="container">
        <div class="section-header">
            <span class="badge-pill">FEATURED WORK</span>
            <h2 class="section-title">Projects & Solutions</h2>
            <p class="section-subtitle">A selection of projects showcasing expertise in full-stack development and security.</p>
        </div>

        <div class="projects-grid" id="projectsGrid"></div>
    </div>
</section>`,

    experience: `
    <section id="experience" class="experience-section">
    <div class="container">
        <div class="section-header">
            <span class="badge-pill">JOURNEY</span>
            <h2 class="section-title">Professional Experience</h2>
        </div>

        <div class="timeline" id="experienceTimeline">
            </div>
    </div>
</section>`,

    certifications: `
    <section id="certifications" class="credentials-section">
    <div class="container">
        <div class="section-header text-center">
            <span class="badge-pill">CREDENTIALS</span>
            <h2 class="section-title">Certifications & Skills</h2>
            <p class="section-subtitle">Industry-recognized certifications and comprehensive technical expertise</p>
        </div>

        <h3 class="sub-section-title">Professional Certifications</h3>
        <div class="certs-grid" id="certsGrid"></div>

        <h3 class="sub-section-title">Technical Skills</h3>
        <div class="skills-grid" id="skillsGrid"></div>
    </div>
</section>`,

    blog: `
    <section id="blog" class="blog-section">
    <div class="container">
        <div class="section-header text-center">
            <span class="badge-pill">INSIGHTS & ARTICLES</span>
            <h2 class="section-title">Latest Blog Posts</h2>
            <p class="section-subtitle">Thoughts on technology, security, and building better software</p>
        </div>

        <div class="blog-grid" id="blogGrid">
            </div>

        <div class="text-center mt-5">
            <a href="#" class="btn-blog-outline">
                View All Articles <i class="bi bi-arrow-right"></i>
            </a>
        </div>
    </div>
</section>`,

    contact: `
    <section id="contact" class="contact-section">
    <div class="container">
        <div class="section-header text-center">
            <span class="badge-pill">GET IN TOUCH</span>
            <h2 class="section-title">Let's Build Something Secure</h2>
            <p class="section-subtitle">Ready to discuss your next project? I'm always open to new opportunities and collaborations.</p>
        </div>

        <div class="contact-grid">
            <div class="contact-sidebar">
                <div class="info-card shadow-sm" id="contactInfo">
                    </div>
                <div class="status-card shadow-sm">
                    <p>Based in Nairobi, available for remote opportunities worldwide. Specializing in secure full-stack development and cybersecurity consulting.</p>
                </div>
            </div>

            <div class="contact-form-card shadow-sm">
                <form id="portfolioContactForm">
                    <div class="form-row">
                        <div class="form-group">
                            <label>Your Name</label>
                            <input type="text" name="name" placeholder="John Doe" required>
                        </div>
                        <div class="form-group">
                            <label>Your Email</label>
                            <input type="email" name="email" placeholder="john@example.com" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Subject</label>
                        <input type="text" name="subject" placeholder="Project Discussion" required>
                    </div>
                    <div class="form-group">
                        <label>Message</label>
                        <textarea name="message" rows="5" placeholder="Tell me about your project..." required></textarea>
                    </div>
                    <button type="submit" class="btn-submit">
                        Send Message <i class="bi bi-send"></i>
                    </button>
                </form>
            </div>
        </div>

        <div class="footer-cta text-center">
            <h3>Let's create something <span class="text-blue">secure</span> and <span class="text-blue">remarkable</span></h3>
            <p>Open to freelance projects, consulting, and full-time opportunities.</p>
        </div>
    </div>
</section>`
};