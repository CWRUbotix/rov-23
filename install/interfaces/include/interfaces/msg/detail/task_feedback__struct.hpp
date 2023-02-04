// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/TaskFeedback.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__TaskFeedback __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__TaskFeedback __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TaskFeedback_
{
  using Type = TaskFeedback_<ContainerAllocator>;

  explicit TaskFeedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->task_id = 0ll;
    }
  }

  explicit TaskFeedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    interfaces::msg::TaskFeedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::TaskFeedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::TaskFeedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::TaskFeedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__TaskFeedback
    std::shared_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__TaskFeedback
    std::shared_ptr<interfaces::msg::TaskFeedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskFeedback_ & other) const
  {
    if (this->task_id != other.task_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskFeedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskFeedback_

// alias to use template instance with default allocator
using TaskFeedback =
  interfaces::msg::TaskFeedback_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__TASK_FEEDBACK__STRUCT_HPP_
