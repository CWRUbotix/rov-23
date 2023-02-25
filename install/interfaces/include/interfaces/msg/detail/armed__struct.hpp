// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Armed.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ARMED__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__ARMED__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Armed __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Armed __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Armed_
{
  using Type = Armed_<ContainerAllocator>;

  explicit Armed_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->armed = false;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->armed = false;
    }
  }

  explicit Armed_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->armed = false;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->armed = false;
    }
  }

  // field types and members
  using _armed_type =
    bool;
  _armed_type armed;

  // setters for named parameter idiom
  Type & set__armed(
    const bool & _arg)
  {
    this->armed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Armed_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Armed_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Armed_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Armed_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Armed_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Armed_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Armed_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Armed_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Armed_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Armed_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Armed
    std::shared_ptr<interfaces::msg::Armed_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Armed
    std::shared_ptr<interfaces::msg::Armed_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armed_ & other) const
  {
    if (this->armed != other.armed) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armed_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armed_

// alias to use template instance with default allocator
using Armed =
  interfaces::msg::Armed_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ARMED__STRUCT_HPP_
