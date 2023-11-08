
FROM ubuntu

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server python3 python3-pip sudo

RUN mkdir /var/run/sshd
# Set root password
RUN echo 'root:test' | chpasswd

# Create test user with password test
RUN useradd -m test && echo 'test:test' | chpasswd

# Allow SSH access for test user
RUN mkdir /home/test/.ssh
COPY ./id_rsa.pub /home/test/.ssh/authorized_keys
RUN chown -R test:test /home/test/.ssh && chmod 700 /home/test/.ssh && chmod 600 /home/test/.ssh/authorized_keys

# Add test user to sudo group
RUN usermod -aG sudo test

EXPOSE 22
EXPOSE 80
# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]
