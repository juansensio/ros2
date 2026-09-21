run:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

bash:
	docker exec -it ros2-jazzy bash