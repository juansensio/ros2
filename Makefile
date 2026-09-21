run:
	docker compose up -d

down:
	docker compose down

bash:
	docker exec -it ros2-jazzy bash