@REM REMOVE ALL IMAGES: docker image prune -a

@REM RUN ONCE: Create container and run it
@REM docker run -it personal-manager

@REM START CONTAINER
docker start personal-manager
@REM EXEC COMMAND "personal-manager" IN CONTAINER AND BOUND TERMINAL
docker container exec -it personal-manager personal-manager
@REM STOP CONTAINER
docker stop personal-manager
