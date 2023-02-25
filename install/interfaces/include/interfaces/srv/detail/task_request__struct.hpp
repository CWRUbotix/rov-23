// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/TaskRequest.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TASK_REQUEST__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__TASK_REQUEST__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__TaskRequest_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__TaskRequest_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskRequest_Request_
{
  using Type = TaskRequest_Request_<ContainerAllocator>;

  explicit TaskRequest_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->task_id = 0ll;
    }
  }

  explicit TaskRequest_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->task_id = 0ll;
    }
  }

  // field types and members
  using _task_id_type =
    int64_t;
  _task_id_type task_id;

  // setters for named parameter idiom
  Type & set__task_id(
    const int64_t & _arg)
  {
    this->task_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::TaskRequest_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::TaskRequest_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::TaskRequest_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::TaskRequest_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__TaskRequest_Request
    std::shared_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__TaskRequest_Request
    std::shared_ptr<interfaces::srv::TaskRequest_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskRequest_Request_ & other) const
  {
    if (this->task_id != other.task_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskRequest_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskRequest_Request_

// alias to use template instance with default allocator
using TaskRequest_Request =
  interfaces::srv::TaskRequest_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__TaskRequest_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__TaskRequest_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskRequest_Response_
{
  using Type = TaskRequest_Response_<ContainerAllocator>;

  explicit TaskRequest_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = "";
    }
  }

  explicit TaskRequest_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : response(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = "";
    }
  }

  // field types and members
  using _response_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__response(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::TaskRequest_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::TaskRequest_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::TaskRequest_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::TaskRequest_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__TaskRequest_Response
    std::shared_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__TaskRequest_Response
    std::shared_ptr<interfaces::srv::TaskRequest_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskRequest_Response_ & other) const
  {
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskRequest_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskRequest_Response_

// alias to use template instance with default allocator
using TaskRequest_Response =
  interfaces::srv::TaskRequest_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct TaskRequest
{
  using Request = interfaces::srv::TaskRequest_Request;
  using Response = interfaces::srv::TaskRequest_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__TASK_REQUEST__STRUCT_HPP_
