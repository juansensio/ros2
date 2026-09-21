run:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

bash:
	docker exec -it ros2-jazzy bash -c "\
		source /opt/ros/jazzy/setup.bash && \
		cd /root/ros2_ws && \
		source install/setup.bash && \
		exec bash \
	"