nvidia-docker run --rm   --name job_analysis  \
                    -v /home/usagi/work/Job_Analysis:/tf/usagi  \
                    -p 9009:8888 -w /tf/usagi  \
                    --user root -e GRANT_SUDO=YES  \

#-u 1000:1000  \
