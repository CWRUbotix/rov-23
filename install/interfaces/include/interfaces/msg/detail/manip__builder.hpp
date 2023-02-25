// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Manip.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MANIP__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__MANIP__BUILDER_HPP_

#include "interfaces/msg/detail/manip__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Manip_activated
{
public:
  explicit Init_Manip_activated(::interfaces::msg::Manip & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Manip activated(::interfaces::msg::Manip::_activated_type arg)
  {
    msg_.activated = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Manip msg_;
};

class Init_Manip_manip_id
{
public:
  Init_Manip_manip_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Manip_activated manip_id(::interfaces::msg::Manip::_manip_id_type arg)
  {
    msg_.manip_id = std::move(arg);
    return Init_Manip_activated(msg_);
  }

private:
  ::interfaces::msg::Manip msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Manip>()
{
  return interfaces::msg::builder::Init_Manip_manip_id();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__MANIP__BUILDER_HPP_
