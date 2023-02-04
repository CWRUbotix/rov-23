// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/ManipService.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MANIP_SERVICE__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__MANIP_SERVICE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__ManipService_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__ManipService_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ManipService_Request_
{
  using Type = ManipService_Request_<ContainerAllocator>;

  explicit ManipService_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manip_id = 0ll;
      this->activated = false;
    }
  }

  explicit ManipService_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manip_id = 0ll;
      this->activated = false;
    }
  }

  // field types and members
  using _manip_id_type =
    int64_t;
  _manip_id_type manip_id;
  using _activated_type =
    bool;
  _activated_type activated;

  // setters for named parameter idiom
  Type & set__manip_id(
    const int64_t & _arg)
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
    interfaces::srv::ManipService_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::ManipService_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ManipService_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ManipService_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__ManipService_Request
    std::shared_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__ManipService_Request
    std::shared_ptr<interfaces::srv::ManipService_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ManipService_Request_ & other) const
  {
    if (this->manip_id != other.manip_id) {
      return false;
    }
    if (this->activated != other.activated) {
      return false;
    }
    return true;
  }
  bool operator!=(const ManipService_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ManipService_Request_

// alias to use template instance with default allocator
using ManipService_Request =
  interfaces::srv::ManipService_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__ManipService_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__ManipService_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ManipService_Response_
{
  using Type = ManipService_Response_<ContainerAllocator>;

  explicit ManipService_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit ManipService_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::ManipService_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::ManipService_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ManipService_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ManipService_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__ManipService_Response
    std::shared_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__ManipService_Response
    std::shared_ptr<interfaces::srv::ManipService_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ManipService_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const ManipService_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ManipService_Response_

// alias to use template instance with default allocator
using ManipService_Response =
  interfaces::srv::ManipService_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct ManipService
{
  using Request = interfaces::srv::ManipService_Request;
  using Response = interfaces::srv::ManipService_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MANIP_SERVICE__STRUCT_HPP_
