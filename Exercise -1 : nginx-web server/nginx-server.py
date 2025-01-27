import subprocess
import os

def install_nginx():
    """Install NGINX on the Raspberry Pi."""
    try:
        print("Installing NGINX on Raspberry Pi...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "nginx"], check=True)
        print("NGINX installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        exit(1)

def configure_nginx():
    """Create a simple configuration for the NGINX web server."""
    config = """
server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.html;
    }
}
"""
    try:
        print("Configuring NGINX...")
        config_path = "/etc/nginx/sites-available/default"
        with open(config_path, "w") as f:
            f.write(config)

        print("Reloading NGINX with new configuration...")
        subprocess.run(["sudo", "systemctl", "restart", "nginx"], check=True)
        print("NGINX restarted successfully.")
    except Exception as e:
        print(f"Error during configuration: {e}")
        exit(1)

def create_sample_website():
    """Create a sample HTML file to serve."""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Welcome to NGINX on Raspberry Pi</title>
</head>
<body>
    <h1>NGINX is running on your Raspberry Pi!</h1>
    <p>This is a sample page served by your NGINX server.</p>
</body>
</html>
"""
    try:
        print("Creating sample website...")
        website_path = "/var/www/html/index.html"
        os.makedirs(os.path.dirname(website_path), exist_ok=True)
        with open(website_path, "w") as f:
            f.write(html_content)
        print("Sample website created successfully.")
    except Exception as e:
        print(f"Error creating sample website: {e}")
        exit(1)

def start_nginx():
    """Ensure the NGINX service is running."""
    try:
        print("Starting NGINX service...")
        subprocess.run(["sudo", "systemctl", "start", "nginx"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "nginx"], check=True)
        print("NGINX service started and enabled on boot.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting NGINX service: {e}")
        exit(1)

def main():
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        exit(1)

    install_nginx()
    configure_nginx()
    create_sample_website()
    start_nginx()

    print("NGINX server is running on your Raspberry Pi. You can access it at http://<your_raspberry_pi_ip_address>")

if __name__ == "__main__":
    main()
