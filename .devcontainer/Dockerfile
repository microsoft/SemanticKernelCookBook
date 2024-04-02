FROM mcr.microsoft.com/devcontainers/miniconda:0-3


ENV JAVA_HOME=/usr/local/sdkman/candidates/java/21.0.2-tem/
ENV PATH=$PATH:JAVA_HOME/bin
ENV PATH=$PATH:/usr/share/dotnet

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
RUN pip install jbang

CMD [ "python", "./jbang.py"]

# RUN wget https://github.com/padreati/rapaio-jupyter-kernel/releases/download/1.3.0/rapaio-jupyter-kernel-1.3.0.jar  \
#             && java -jar ./rapaio-jupyter-kernel-1.3.0.jar -i -auto

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
