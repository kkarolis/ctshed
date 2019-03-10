FROM ubuntu:16.04
COPY entrypoint /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
#FIXME exit with error when theres no command
CMD ["echo", "hi"]
