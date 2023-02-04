// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/TaskFeedback.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__TASK_FEEDBACK__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__TASK_FEEDBACK__BUILDER_HPP_

#include "interfaces/msg/detail/task_feedback__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_TaskFeedback_task_id
{
public:
  Init_TaskFeedback_task_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::TaskFeedback task_id(::interfaces::msg::TaskFeedback::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::TaskFeedback msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::TaskFeedback>()
{
  return interfaces::msg::builder::Init_TaskFeedback_task_id();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__TASK_FEEDBACK__BUILDER_HPP_
