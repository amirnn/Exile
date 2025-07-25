find_package(opengl_system REQUIRED)

find_package(glad REQUIRED)
include_directories(${glad_INCLUDE_DIRS})

find_package(glfw3 REQUIRED)
include_directories(${glfw3_INCLUDE_DIRS})

find_package(Eigen3 REQUIRED)
include_directories(${Eigen3_INCLUDE_DIRS})
