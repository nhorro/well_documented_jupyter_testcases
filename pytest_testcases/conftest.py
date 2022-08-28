import pytest
import docker
import time

import pytest

@pytest.fixture()
def calculator_service():

    # Start docker
    client = docker.from_env()
    # docker run --rm --name calculator -p 80:80 calculator-service:latest
    print("Starting docker")
    container = client.containers.run(
        "calculator-service:latest", 
        auto_remove=True,
        ports={'80/tcp': 80},
        detach=True
    )
    
    # Wait for container to start running
    timeout = 10.
    stop_time = 0.5
    elapsed_time = 0.
    while container.status != 'running' and elapsed_time < timeout:
        time.sleep(stop_time)
        elapsed_time += stop_time
        continue
    yield "calculator_service"

    # Cleanup
    print("teardown")
    container.stop()