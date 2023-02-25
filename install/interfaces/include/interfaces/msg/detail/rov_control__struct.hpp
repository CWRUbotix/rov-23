// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/ROVControl.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__msg__ROVControl __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__ROVControl __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ROVControl_
{
  using Type = ROVControl_<ContainerAllocator>;

  explicit ROVControl_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->x = 1500;
      this->y = 1500;
      this->z = 1500;
      this->yaw = 1500;
      this->pitch = 1500;
      this->roll = 1500;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->x = 0;
      this->y = 0;
      this->z = 0;
      this->yaw = 0;
      this->pitch = 0;
      this->roll = 0;
    }
  }

  explicit ROVControl_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->x = 1500;
      this->y = 1500;
      this->z = 1500;
      this->yaw = 1500;
      this->pitch = 1500;
      this->roll = 1500;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->x = 0;
      this->y = 0;
      this->z = 0;
      this->yaw = 0;
      this->pitch = 0;
      this->roll = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _x_type =
    int16_t;
  _x_type x;
  using _y_type =
    int16_t;
  _y_type y;
  using _z_type =
    int16_t;
  _z_type z;
  using _yaw_type =
    int16_t;
  _yaw_type yaw;
  using _pitch_type =
    int16_t;
  _pitch_type pitch;
  using _roll_type =
    int16_t;
  _roll_type roll;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__x(
    const int16_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const int16_t & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const int16_t & _arg)
  {
    this->z = _arg;
    return *this;
  }
  Type & set__yaw(
    const int16_t & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__pitch(
    const int16_t & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__roll(
    const int16_t & _arg)
  {
    this->roll = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::ROVControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::ROVControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::ROVControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::ROVControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ROVControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ROVControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ROVControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ROVControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::ROVControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::ROVControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__ROVControl
    std::shared_ptr<interfaces::msg::ROVControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__ROVControl
    std::shared_ptr<interfaces::msg::ROVControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ROVControl_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->roll != other.roll) {
      return false;
    }
    return true;
  }
  bool operator!=(const ROVControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ROVControl_

// alias to use template instance with default allocator
using ROVControl =
  interfaces::msg::ROVControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ROV_CONTROL__STRUCT_HPP_
