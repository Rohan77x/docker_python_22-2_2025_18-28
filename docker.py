import subprocess

def deploy_container_with_shell(image_name, container_name, host_port, container_port):
    try:
        # Pull Docker image
        print(f"Pulling image: {image_name}...")
        pull_result = subprocess.run(["docker", "pull", image_name], capture_output=True, text=True)
        print(pull_result.stdout)

        # Run Docker container
        print(f"Running container '{container_name}'...")
        run_result = subprocess.run([
            "docker", "run", "-d",
            "--name", container_name,
            "-p", f"{host_port}:{container_port}",
            image_name
        ], capture_output=True, text=True)
        
        if run_result.returncode == 0:
            print(f"Container '{container_name}' started successfully.")
        else:
            print(f"Error running container: {run_result.stderr}")

        # Display container logs
        print(f"Fetching logs for '{container_name}'...")
        logs_result = subprocess.run(["docker", "logs", container_name], capture_output=True, text=True)
        print(logs_result.stdout)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image = "nginx:latest"
    container = "nginx_test"
    host_port = 8080
    container_port = 80
    
    deploy_container_with_shell(image, container, host_port, container_port)
