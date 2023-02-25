// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/TaskRequest.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TASK_REQUEST__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__TASK_REQUEST__TRAITS_HPP_

#include "interfaces/srv/detail/task_request__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::srv::TaskRequest_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: task_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_id: ";
    value_to_yaml(msg.task_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::srv::TaskRequest_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::srv::TaskRequest_Request>()
{
  return "interfaces::srv::TaskRequest_Request";
}

template<>
inline const char * name<interfaces::srv::TaskRequest_Request>()
{
  return "interfaces/srv/TaskRequest_Request";
}

template<>
struct has_fixed_size<interfaces::srv::TaskRequest_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::TaskRequest_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::TaskRequest_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::srv::TaskRequest_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "response: ";
    value_to_yaml(msg.response, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::srv::TaskRequest_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::srv::TaskRequest_Response>()
{
  return "interfaces::srv::TaskRequest_Response";
}

template<>
inline const char * name<interfaces::srv::TaskRequest_Response>()
{
  return "interfaces/srv/TaskRequest_Response";
}

template<>
struct has_fixed_size<interfaces::srv::TaskRequest_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::srv::TaskRequest_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces::srv::TaskRequest_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::TaskRequest>()
{
  return "interfaces::srv::TaskRequest";
}

template<>
inline const char * name<interfaces::srv::TaskRequest>()
{
  return "interfaces/srv/TaskRequest";
}

template<>
struct has_fixed_size<interfaces::srv::TaskRequest>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::TaskRequest_Request>::value &&
    has_fixed_size<interfaces::srv::TaskRequest_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::TaskRequest>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::TaskRequest_Request>::value &&
    has_bounded_size<interfaces::srv::TaskRequest_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::TaskRequest>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::TaskRequest_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::TaskRequest_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__TASK_REQUEST__TRAITS_HPP_
