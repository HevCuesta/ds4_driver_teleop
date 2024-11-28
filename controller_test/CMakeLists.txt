cmake_minimum_required(VERSION 3.8)
project(controller_test)

# Opciones del compilador
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encontrar dependencias
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(controller_interface REQUIRED)

# Añadir ejecutable
add_executable(controller_test_node src/controller_test.cpp)

# Añadir directorios de inclusión
target_include_directories(controller_test_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

# Añadir dependencias al ejecutable
ament_target_dependencies(controller_test_node
  rclcpp
  sensor_msgs
  controller_interface
)

# Instalar ejecutable
install(TARGETS controller_test_node
  DESTINATION lib/${PROJECT_NAME}
)

# Instalar archivos de encabezado (opcional)
install(DIRECTORY include/
  DESTINATION include/
)

install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Empaquetado
ament_package()
