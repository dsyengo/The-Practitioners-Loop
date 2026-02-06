const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const icon = hamburger.querySelector('i');

hamburger.addEventListener('click', () => {
    // Toggle the menu
    navLinks.classList.toggle('active');

    // Toggle the icon between List and Close (X)
    if (navLinks.classList.contains('active')) {
        icon.classList.remove('bi-list');
        icon.classList.add('bi-x-lg');
    } else {
        icon.classList.remove('bi-x-lg');
        icon.classList.add('bi-list');
    }
});

// Close menu when a link is clicked
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        icon.classList.remove('bi-x-lg');
        icon.classList.add('bi-list');
    });
});

// Simple Scroll Observer for Progress Bars
const observerOptions = {
    threshold: 0.5
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const progressFills = entry.target.querySelectorAll('.progress-fill');
            progressFills.forEach(fill => {
                const targetWidth = fill.style.width;
                fill.style.width = '0'; // Reset
                setTimeout(() => fill.style.width = targetWidth, 100);
            });
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

const aboutSection = document.querySelector('.about-section');
if (aboutSection) observer.observe(aboutSection);

const projects = [
    {
        title: "CyberPolicy Pro",
        category: "Featured",
        description: "A comprehensive compliance management system for businesses to track cybersecurity policies, conduct risk assessments, and ensure regulatory compliance.",
        image: "https://plus.unsplash.com/premium_photo-1661497281000-b5ecb39a2114?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9saWN5fGVufDB8fDB8fHwwassets/cyberpolicy.jpg",
        tags: ["Node.js", "React", "MongoDB", "Express", "JWT"],
        codeLink: "#", // Add your GitHub link
        demoLink: "#"  // Add your Live Demo link
    },
    {
        title: "AI Health Assistant",
        category: "Featured",
        description: "An intelligent personal health assistant powered by machine learning that provides personalized health recommendations and tracks wellness metrics.",
        image: "https://images.unsplash.com/photo-1767966769495-dbb5e14cab5f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8QUklMjBIZWFsdGglMjBBc3Npc3RhbnR8ZW58MHx8MHx8fDA%3D",
        tags: ["Python", "TensorFlow", "React Native", "FastAPI", "PostgreSQL"],
        codeLink: "#",
        demoLink: "#"
    },
    {
        title: "Smart Air Quality Monitor",
        category: "Featured",
        description: "IoT-based monitoring system with AI analytics, developed for the Huawei ICT Competition 2024-2025 Global Finals.",
        image: "https://plus.unsplash.com/premium_photo-1714510332132-b3074b75a312?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8U21hcnQlMjBBaXIlMjBRdWFsaXR5JTIwTW9uaXRvcnxlbnwwfHwwfHx8MA%3D%3D",
        tags: ["IoT", "Python", "Machine Learning", "Huawei Cloud", "React"],
        codeLink: "#",
        demoLink: "#"
    }
];

function renderProjects() {
    const grid = document.getElementById('projectsGrid');
    if (!grid) return;

    grid.innerHTML = projects.map(project => `
        <div class="project-card">
            <div class="project-image">
                <img src="${project.image}" alt="${project.title}">
                <span class="project-badge">${project.category}</span>
            </div>
            <div class="project-info">
                <h3>${project.title}</h3>
                <p>${project.description}</p>
                <div class="project-tags">
                    ${project.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
                <div class="project-links">
                    <a href="${project.codeLink}" class="link-icon"><i class="bi bi-github"></i> Code</a>
                    <a href="${project.demoLink}" class="link-icon"><i class="bi bi-box-arrow-up-right"></i> Live Demo</a>
                </div>
            </div>
        </div>
    `).join('');
}

const experiences = [
    {
        role: "DevOps Intern - ISCS Department",
        company: "Konza Technopolis Development Authority",
        period: "Jan 2026 - Present",
        description: "Placed by ICT Authority (PDTP Program). Contributing to the full lifecycle management of enterprise systems—from requirements analysis to deployment and operational support—while implementing DevOps practices for system reliability.",
        highlights: ["System Reliability", "Automation", "Operational Support"]
    },
    {
        role: "ICT Attachment Attaché",
        company: "Ministry of Roads, Public Works and Transport",
        period: "May 2024 - July 2024",
        description: "Supported government ICT infrastructure in Kitui County by delivering end-user training, troubleshooting hardware and network issues, and maintaining software systems.",
        highlights: ["Network Troubleshooting", "User Support", "Infrastructure Maintenance"]
    }
];

// Re-using the render function we established
function renderExperience() {
    const timeline = document.getElementById('experienceTimeline');
    if (!timeline) return;

    timeline.innerHTML = experiences.map((exp, index) => `
        <div class="timeline-item ${index % 2 === 0 ? 'left' : 'right'}">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <span class="exp-date">${exp.period}</span>
                <h3>${exp.role}</h3>
                <h4>${exp.company}</h4>
                <p>${exp.description}</p>
                <div class="exp-highlights">
                    ${exp.highlights.map(h => `<span class="h-pill">${h}</span>`).join('')}
                </div>
            </div>
        </div>
    `).join('');
}



// Data for Professional Certifications
// Data for Professional Certifications
const professionalCerts = [
    {
        title: "Huawei ICT Competition",
        description: "Third Prize Global Finalist - Innovation Track: Smart Air Quality Monitoring System leveraging AI and IoTDA.",
        issuer: "Huawei",
        year: "2025",
        icon: "bi-trophy",
        color: "#ef4444" // Huawei Red
    },
    {
        title: "Certified in Cybersecurity",
        description: "CC (ISC)²: Principles, Access Control, Network Security, Risk Management, and Incident Response.",
        issuer: "ISC²",
        year: "2024",
        icon: "bi-shield-check",
        color: "#007bff" // ISC2 Blue
    },
    {
        title: "Creating Compelling Reports",
        description: "Structuring technical content and presenting data effectively for business and IT environments.",
        issuer: "Cisco Networking Academy",
        year: "2026",
        icon: "bi-file-earmark-text",
        color: "#00bceb" // Cisco Blue
    },
    {
        title: "Digital Awareness",
        description: "Foundational knowledge in digital literacy, data privacy, and responsible technology use.",
        issuer: "Cisco Networking Academy",
        year: "2026",
        icon: "bi-laptop",
        color: "#10b981" // Security Green
    },
    {
        title: "English for IT",
        description: "Professional IT communication, technical documentation, and global team collaboration.",
        issuer: "Cisco Networking Academy",
        year: "2026",
        icon: "bi-translate",
        color: "#6f42c1" // Purple
    }
];

// Data for Technical Skills (Split into two columns per category)
const technicalSkills = [
    {
        category: "Backend Architecture",
        icon: "bi-hdd-network",
        colorClass: "backend-theme",
        col1: ["Node.js", "Django", "Laravel"],
        col2: ["RESTful API Design", "Microservices", "Secure System Design"]
    },
    {
        category: "Frontend & Mobile",
        icon: "bi-phone",
        colorClass: "frontend-theme",
        col1: ["React", "Angular"],
        col2: ["Bootstrap", "Flutter"]
    },
    {
        category: "Databases & Data Systems",
        icon: "bi-database",
        colorClass: "database-theme",
        col1: ["PostgreSQL", "MySQL"],
        col2: ["MongoDB", "DB Design & Opt."]
    },
    {
        category: "Cybersecurity & Security",
        icon: "bi-shield-lock",
        colorClass: "security-theme",
        col1: ["Secure SDLC", "Vulnerability Assessment"],
        col2: ["IAM", "Encryption & Protection"]
    },
    {
        category: "DevOps & Cloud",
        icon: "bi-cloud-arrow-up",
        colorClass: "devops-theme",
        col1: ["Docker", "CI/CD Pipelines", "Linux"],
        col2: ["AWS Deployment", "Automation", "Monitoring"]
    },
    {
        category: "Product & Design",
        icon: "bi-lightbulb",
        colorClass: "product-theme",
        col1: ["UI/UX (Figma)", "System Design"],
        col2: ["Requirements Analysis", "Agile Collaboration"]
    }
];

function renderCredentials() {
    const certsContainer = document.getElementById('certsGrid');
    const skillsContainer = document.getElementById('skillsGrid');

    if (certsContainer) {
        certsContainer.innerHTML = professionalCerts.map(cert => `
            <div class="cert-card-v3">
                <div class="cert-icon-float" style="background: ${cert.color}">
                    <i class="bi ${cert.icon}"></i>
                </div>
                <div class="cert-body">
                    <h3>${cert.title}</h3>
                    <p class="cert-desc">${cert.description}</p>
                    <div class="cert-meta">
                        <span class="issuer">${cert.issuer}</span>
                        <span class="year" style="color: ${cert.color}">${cert.year}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    if (skillsContainer) {
        skillsContainer.innerHTML = technicalSkills.map(skill => `
            <div class="skill-detail-card">
                <div class="skill-card-head ${skill.colorClass}">
                    <i class="bi ${skill.icon}"></i>
                    <h4>${skill.category}</h4>
                </div>
                <div class="skill-columns">
                    <ul>${skill.col1.map(s => `<li>${s}</li>`).join('')}</ul>
                    <ul>${skill.col2.map(s => `<li>${s}</li>`).join('')}</ul>
                </div>
            </div>
        `).join('');
    }
}

const blogPosts = [
    {
        title: "Zero-Trust Architecture: A Modern Security",
        category: "Security",
        date: "January 20, 2026",
        readTime: "8 min read",
        excerpt: "Exploring how zero-trust security models are reshaping enterprise application architecture and why...",
        image: "https://images.unsplash.com/photo-1762340916350-ad5a3d620c16?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y3liZXIlMjBkZWZlbnNlfGVufDB8fDB8fHww", // Path to your blog image
        color: "#6f42c1"
    },
    {
        title: "Building Scalable Microservices with",
        category: "Development",
        date: "January 15, 2026",
        readTime: "12 min read",
        excerpt: "A comprehensive guide to designing and implementing microservices architecture using...",
        image: "https://plus.unsplash.com/premium_photo-1745306842355-76a97ed6d803?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8QnVpbGRpbmclMjBTY2FsYWJsZSUyME1pY3Jvc2VydmljZXN8ZW58MHx8MHx8fDA%3D",
        color: "#007bff"
    },
    {
        title: "The Rise of AI in Cybersecurity:",
        category: "AI & Security",
        date: "January 10, 2026",
        readTime: "10 min read",
        excerpt: "How artificial intelligence and machine learning are transforming threat detection and response in...",
        image: "https://plus.unsplash.com/premium_photo-1768571046962-f2b12481ad53?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8VGhlJTIwUmlzZSUyMG9mJTIwQUklMjBpbiUyMEN5YmVyc2VjdXJpdHl8ZW58MHx8MHx8fDA%3D",
        color: "#d63384"
    }
];

function renderBlog() {
    const grid = document.getElementById('blogGrid');
    if (!grid) return;

    grid.innerHTML = blogPosts.map(post => `
        <div class="blog-card">
            <div class="blog-image">
                <img src="${post.image}" alt="${post.title}">
                <span class="blog-category" style="background: ${post.color}">${post.category}</span>
            </div>
            <div class="blog-body">
                <div class="blog-meta">
                    <span><i class="bi bi-calendar3"></i> ${post.date}</span>
                    <span><i class="bi bi-clock"></i> ${post.readTime}</span>
                </div>
                <h3 class="blog-title">${post.title}</h3>
                <p class="blog-excerpt">${post.excerpt}</p>
                <a href="#" class="read-more" style="color: ${post.color}">
                    Read More <i class="bi bi-arrow-right"></i>
                </a>
            </div>
        </div>
    `).join('');
}

const contactDetails = {
    email: "deniswilson028@gmail.com|| dsyengo@konza.ke",
    phone: "+254 115 014 027",
    location: "Nairobi, Kenya"
};

function renderContact() {
    const container = document.getElementById('contactInfo');
    if (!container) return;

    container.innerHTML = `
        <h3 class="fw-bold mb-4">Contact Information</h3>
        <div class="info-item">
            <div class="info-icon blue-bg"><i class="bi bi-envelope"></i></div>
            <div class="info-text">
                <span>Email</span>
                <p>${contactDetails.email}</p>
            </div>
        </div>
        <div class="info-item">
            <div class="info-icon blue-bg"><i class="bi bi-telephone"></i></div>
            <div class="info-text">
                <span>Phone</span>
                <p>${contactDetails.phone}</p>
            </div>
        </div>
        <div class="info-item">
            <div class="info-icon blue-bg"><i class="bi bi-geo-alt"></i></div>
            <div class="info-text">
                <span>Location</span>
                <p>${contactDetails.location}</p>
            </div>
        </div>
    `;
}

// Form Handling Logic
async function handleFormSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('http://localhost:8000', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert("Message sent successfully!");
            e.target.reset();
        } else {
            alert("Server error. Please try again later.");
        }
    } catch (error) {
        console.error("Connection error:", error);
    }
}



// DOM listener
document.addEventListener('DOMContentLoaded', () => {
    // ... previous logic
    renderProjects();
    renderExperience();
    renderCredentials()
    renderBlog();
    renderContact();
    const form = document.getElementById('portfolioContactForm');
    if (form) form.addEventListener('submit', handleFormSubmit);
});