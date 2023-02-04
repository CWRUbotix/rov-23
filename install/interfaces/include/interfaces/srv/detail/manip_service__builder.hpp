// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/ManipService.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MANIP_SERVICE__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__MANIP_SERVICE__BUILDER_HPP_

#include "interfaces/srv/detail/manip_service__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ManipService_Request_activated
{
public:
  explicit Init_ManipService_Request_activated(::interfaces::srv::ManipService_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::ManipService_Request activated(::interfaces::srv::ManipService_Request::_activated_type arg)
  {
    msg_.activated = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ManipService_Request msg_;
};

class Init_ManipService_Request_manip_id
{
public:
  Init_ManipService_Request_manip_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ManipService_Request_activated manip_id(::interfaces::srv::ManipService_Request::_manip_id_type arg)
  {
    msg_.manip_id = std::move(arg);
    return Init_ManipService_Request_activated(msg_);
  }

private:
  ::interfaces::srv::ManipService_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ManipService_Request>()
{
  return interfaces::srv::builder::Init_ManipService_Request_manip_id();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ManipService_Response>()
{
  return ::interfaces::srv::ManipService_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MANIP_SERVICE__BUILDER_HPP_
