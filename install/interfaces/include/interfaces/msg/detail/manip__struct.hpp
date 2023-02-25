// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Manip.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MANIP__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__MANIP__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Manip __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Manip __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Manip_
{
  using Type = Manip_<ContainerAllocator>;

  explicit Manip_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manip_id = "";
      this->activated = false;
    }
  }

  explicit Manip_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : manip_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manip_id = "";
      this->activated = false;
    }
  }

  // field types and members
  using _manip_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _manip_id_type manip_id;
  using _activated_type =
    bool;
  _activated_type activated;

  // setters for named parameter idiom
  Type & set__manip_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->manip_id = _arg;
    return *this;
  }
  Type & set__activated(
    const bool & _arg)
  {
    this->activated = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Manip_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Manip_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Manip_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Manip_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Manip_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Manip_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Manip_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Manip_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Manip_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Manip_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Manip
    std::shared_ptr<interfaces::msg::Manip_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Manip
    std::shared_ptr<interfaces::msg::Manip_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Manip_ & other) const
  {
    if (this->manip_id != other.manip_id) {
      return false;
    }
    if (this->activated != other.activated) {
      return false;
    }
    return true;
  }
  bool operator!=(const Manip_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Manip_

// alias to use template instance with default allocator
using Manip =
  interfaces::msg::Manip_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__MANIP__STRUCT_HPP_
