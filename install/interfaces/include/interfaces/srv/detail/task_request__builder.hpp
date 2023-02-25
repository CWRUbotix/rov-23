// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/TaskRequest.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TASK_REQUEST__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__TASK_REQUEST__BUILDER_HPP_

#include "interfaces/srv/detail/task_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_TaskRequest_Request_task_id
{
public:
  Init_TaskRequest_Request_task_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::TaskRequest_Request task_id(::interfaces::srv::TaskRequest_Request::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::TaskRequest_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::TaskRequest_Request>()
{
  return interfaces::srv::builder::Init_TaskRequest_Request_task_id();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_TaskRequest_Response_response
{
public:
  Init_TaskRequest_Response_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::TaskRequest_Response response(::interfaces::srv::TaskRequest_Response::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::TaskRequest_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::TaskRequest_Response>()
{
  return interfaces::srv::builder::Init_TaskRequest_Response_response();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__TASK_REQUEST__BUILDER_HPP_
