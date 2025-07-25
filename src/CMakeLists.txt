# src

add_executable(exile)
target_sources(exile PRIVATE mypkg.cpp main.cpp)

target_link_libraries(
        exile PRIVATE
        glad::glad 
        glfw
        opengl::opengl 
        Eigen3::Eigen
)

#target_include_directories(
#
#)

# install(TARGETS exile DESTINATION "."
#         RUNTIME DESTINATION bin
#         ARCHIVE DESTINATION lib
#         LIBRARY DESTINATION lib
#         )


# Print Variables
#get_cmake_property(_variableNames VARIABLES)
#list (SORT _variableNames)
#foreach (_variableName ${_variableNames})
#        message(STATUS "${_variableName}=${${_variableName}}")
#endforeach()