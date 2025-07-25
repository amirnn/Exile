# src

add_executable(exile )
target_sources(exile PRIVATE mypkg.cpp main.cpp)

target_link_libraries(
        exile 
        glad::glad 
        glfw 
        opengl::opengl 
        Eigen3::Eigen
        )

# install(TARGETS exile DESTINATION "."
#         RUNTIME DESTINATION bin
#         ARCHIVE DESTINATION lib
#         LIBRARY DESTINATION lib
#         )