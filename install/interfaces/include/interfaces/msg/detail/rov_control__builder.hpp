// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/ROVControl.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ROV_CONTROL__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__ROV_CONTROL__BUILDER_HPP_

#include "interfaces/msg/detail/rov_control__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_ROVControl_roll
{
public:
  explicit Init_ROVControl_roll(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::ROVControl roll(::interfaces::msg::ROVControl::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_pitch
{
public:
  explicit Init_ROVControl_pitch(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  Init_ROVControl_roll pitch(::interfaces::msg::ROVControl::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_ROVControl_roll(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_yaw
{
public:
  explicit Init_ROVControl_yaw(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  Init_ROVControl_pitch yaw(::interfaces::msg::ROVControl::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_ROVControl_pitch(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_z
{
public:
  explicit Init_ROVControl_z(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  Init_ROVControl_yaw z(::interfaces::msg::ROVControl::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_ROVControl_yaw(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_y
{
public:
  explicit Init_ROVControl_y(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  Init_ROVControl_z y(::interfaces::msg::ROVControl::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_ROVControl_z(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_x
{
public:
  explicit Init_ROVControl_x(::interfaces::msg::ROVControl & msg)
  : msg_(msg)
  {}
  Init_ROVControl_y x(::interfaces::msg::ROVControl::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ROVControl_y(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

class Init_ROVControl_header
{
public:
  Init_ROVControl_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ROVControl_x header(::interfaces::msg::ROVControl::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ROVControl_x(msg_);
  }

private:
  ::interfaces::msg::ROVControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::ROVControl>()
{
  return interfaces::msg::builder::Init_ROVControl_header();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ROV_CONTROL__BUILDER_HPP_
