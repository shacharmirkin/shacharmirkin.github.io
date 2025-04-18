---
layout: default
title: Contact
---

# Contact

<div class="contact-container">
    <div class="contact-info">
        <h2>Get in Touch</h2>
        <p>Feel free to reach out to me through any of the following channels:</p>
        
        <div class="contact-methods">
            <div class="contact-method">
                <h3>Email</h3>
                <p><a href="mailto:your.email@example.com">your.email@example.com</a></p>
            </div>
            
            <div class="contact-method">
                <h3>Social Media</h3>
                <div class="social-links">
                    <a href="#" class="social-link">Twitter</a>
                    <a href="#" class="social-link">LinkedIn</a>
                    <a href="#" class="social-link">GitHub</a>
                </div>
            </div>
            
            <div class="contact-method">
                <h3>Office</h3>
                <p>Your Institution Name<br>
                Department Name<br>
                Building Name, Room Number<br>
                City, State ZIP</p>
            </div>
        </div>
    </div>

    <div class="contact-form">
        <h2>Send a Message</h2>
        <form action="#" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
            </div>

            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>

            <button type="submit" class="submit-button">Send Message</button>
        </form>
    </div>

</div>

<style>
.contact-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem 1rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
}

.contact-info h2, .contact-form h2 {
    font-size: 1.75rem;
    margin-bottom: 1.5rem;
    color: var(--text-color);
    border-bottom: 2px solid var(--nav-border);
    padding-bottom: 0.5rem;
}

.contact-methods {
    display: grid;
    gap: 2rem;
}

.contact-method h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--text-color);
}

.contact-method p {
    color: #4b5563;
    line-height: 1.6;
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-link {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: 0.25rem;
    font-size: 0.9rem;
    transition: background-color 0.2s ease;
}

.social-link:hover {
    background-color: var(--secondary-color);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--text-color);
    font-weight: 500;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--nav-border);
    border-radius: 0.25rem;
    font-size: 1rem;
    transition: border-color 0.2s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
}

.submit-button {
    background-color: var(--primary-color);
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 0.25rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.submit-button:hover {
    background-color: var(--secondary-color);
}

@media (max-width: 768px) {
    .contact-container {
        grid-template-columns: 1fr;
        gap: 2rem;
        padding: 1rem;
    }
    
    .social-links {
        flex-wrap: wrap;
    }
}
</style>
