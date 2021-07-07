FROM debian:latest

RUN apt-get -y update && \
    apt-get -y install build-essential autoconf libtool pkg-config git curl cmake

RUN mkdir /grpc-build 
WORKDIR /grpc-build

RUN git clone --recurse-submodules -b v1.38.0 https://github.com/grpc/grpc
RUN cd grpc && \
    mkdir -p cmake/build && \ 
    cd cmake/build && \
    cmake -DgRPC_INSTALL=ON \
      -DgRPC_BUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR \
      ../.. && \
    make -j 2 && \
    make install && \
    cd - && \
    mkdir -p third_party/abseil-cpp/cmake/build && \
    cd third_party/abseil-cpp/cmake/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR \
          -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
          ../.. && \
    make -j 2 && \
    make install && \
    cd -

WORKDIR /grpc-build/grpc
CMD ["bash"]