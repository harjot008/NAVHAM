// Toggle between Login and Sign Up forms
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    const loginForm = document.querySelector('.login-form');
    const authToggle = document.querySelector('.auth-toggle');
    
    let isLoginMode = true;
    
    // Toggle button functionality
    toggleBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            toggleBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            if (index === 0) {
                // Login mode
                isLoginMode = true;
                updateFormForLogin();
            } else {
                // Sign up mode
                isLoginMode = false;
                updateFormForSignup();
            }
        });
    });
    
    function updateFormForLogin() {
        const form = loginForm;
        form.innerHTML = `
            <div class="input-group">
                <input type="email" id="email" name="email" placeholder=" " required>
                <label for="email">Email</label>
            </div>
            <div class="input-group">
                <input type="password" id="password" name="password" placeholder=" " required>
                <label for="password">Password</label>
            </div>
            <button type="submit" class="signin-btn">Sign In</button>
        `;
    }
    
    function updateFormForSignup() {
        const form = loginForm;
        form.innerHTML = `
            <div class="input-group">
                <input type="text" id="name" name="name" placeholder=" " required>
                <label for="name">Full Name</label>
            </div>
            <div class="input-group">
                <input type="email" id="email" name="email" placeholder=" " required>
                <label for="email">Email</label>
            </div>
            <div class="input-group">
                <input type="password" id="password" name="password" placeholder=" " required>
                <label for="password">Password</label>
            </div>
            <div class="input-group">
                <input type="password" id="confirmPassword" name="confirmPassword" placeholder=" " required>
                <label for="confirmPassword">Confirm Password</label>
            </div>
            <button type="submit" class="signin-btn">Create Account</button>
        `;
    }
    
    // Form submission handler
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        
        if (isLoginMode) {
            await handleLogin(data);
        } else {
            await handleSignup(data);
        }
    });
    
    async function handleLogin(data) {
        try {
            showLoading();
            
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: data.email,
                    password: data.password
                })
            });
            
            const result = await response.json();
            
            if (result.success) {
                showMessage(result.message, 'success');
                // Redirect after a short delay
                setTimeout(() => {
                    window.location.href = result.redirect;
                }, 1000);
            } else {
                showMessage(result.message, 'error');
            }
        } catch (error) {
            showMessage('Login failed. Please check your connection.', 'error');
        } finally {
            hideLoading();
        }
    }
    
    async function handleSignup(data) {
        // Validate password confirmation
        if (data.password !== data.confirmPassword) {
            showMessage('Passwords do not match', 'error');
            return;
        }
        
        // Basic password validation
        if (data.password.length < 6) {
            showMessage('Password must be at least 6 characters long', 'error');
            return;
        }
        
        try {
            showLoading();
            
            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name: data.name,
                    email: data.email,
                    password: data.password
                })
            });
            
            const result = await response.json();
            
            if (result.success) {
                showMessage(result.message, 'success');
                // Redirect after a short delay
                setTimeout(() => {
                    window.location.href = result.redirect;
                }, 1000);
            } else {
                showMessage(result.message, 'error');
            }
        } catch (error) {
            showMessage('Registration failed. Please check your connection.', 'error');
        } finally {
            hideLoading();
        }
    }
    
    function showMessage(message, type) {
        // Remove existing messages
        const existingMessage = document.querySelector('.auth-message');
        if (existingMessage) {
            existingMessage.remove();
        }
        
        // Create new message element
        const messageEl = document.createElement('div');
        messageEl.className = `auth-message ${type}`;
        messageEl.textContent = message;
        messageEl.style.cssText = `
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            text-align: center;
            font-size: 14px;
            ${type === 'success' ? 'background: #d4edda; color: #155724; border: 1px solid #c3e6cb;' : 'background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;'}
        `;
        
        // Insert before the form
        loginForm.parentNode.insertBefore(messageEl, loginForm);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (messageEl && messageEl.parentNode) {
                messageEl.remove();
            }
        }, 5000);
    }
    
    function showLoading() {
        const submitBtn = loginForm.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Loading...';
        }
    }
    
    function hideLoading() {
        const submitBtn = loginForm.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = isLoginMode ? 'Sign In' : 'Create Account';
        }
    }
});