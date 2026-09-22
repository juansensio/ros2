FROM ros:jazzy

WORKDIR /root/ros2_ws

RUN apt update && apt install -y \
    ros-jazzy-demo-nodes-cpp \
    ros-jazzy-demo-nodes-py \
    python3-colcon-common-extensions \
    zsh \
    git \
    vim \
    curl

# Install Oh My Zsh non-interactively
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install zsh plugins
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Add plugins to .zshrc
RUN sed -i 's/plugins=(git)/plugins=(\n  git\n  zsh-autosuggestions\n  zsh-syntax-highlighting\n)/' /root/.zshrc

# Set zsh as default shell
RUN chsh -s $(which zsh) root

# alias
RUN echo "alias c='clear'" >> /root/.zshrc
RUN echo "alias r2='ros2'" >> /root/.zshrc
RUN echo "alias r2r='ros2 run'" >> /root/.zshrc
RUN echo "alias r2i='ros2 info'" >> /root/.zshrc
RUN echo "alias rb='rm -rf build install log'" >> /root/.zshrc
RUN echo "alias cb='colcon build --symlink-install'" >> /root/.zshrc
RUN echo "alias si='source install/setup.zsh'" >> /root/.zshrc