// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Armed.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ARMED__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__ARMED__BUILDER_HPP_

#include "interfaces/msg/detail/armed__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Armed_armed
{
public:
  Init_Armed_armed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::Armed armed(::interfaces::msg::Armed::_armed_type arg)
  {
    msg_.armed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Armed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Armed>()
{
  return interfaces::msg::builder::Init_Armed_armed();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ARMED__BUILDER_HPP_
