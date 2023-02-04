// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/ManipService.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MANIP_SERVICE__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__MANIP_SERVICE__TRAITS_HPP_

#include "interfaces/srv/detail/manip_service__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::srv::ManipService_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: manip_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "manip_id: ";
    value_to_yaml(msg.manip_id, out);
    out << "\n";
  }

  // member: activated
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "activated: ";
    value_to_yaml(msg.activated, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::srv::ManipService_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::srv::ManipService_Request>()
{
  return "interfaces::srv::ManipService_Request";
}

template<>
inline const char * name<interfaces::srv::ManipService_Request>()
{
  return "interfaces/srv/ManipService_Request";
}

template<>
struct has_fixed_size<interfaces::srv::ManipService_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::ManipService_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::ManipService_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const interfaces::srv::ManipService_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const interfaces::srv::ManipService_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<interfaces::srv::ManipService_Response>()
{
  return "interfaces::srv::ManipService_Response";
}

template<>
inline const char * name<interfaces::srv::ManipService_Response>()
{
  return "interfaces/srv/ManipService_Response";
}

template<>
struct has_fixed_size<interfaces::srv::ManipService_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::ManipService_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::ManipService_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::ManipService>()
{
  return "interfaces::srv::ManipService";
}

template<>
inline const char * name<interfaces::srv::ManipService>()
{
  return "interfaces/srv/ManipService";
}

template<>
struct has_fixed_size<interfaces::srv::ManipService>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::ManipService_Request>::value &&
    has_fixed_size<interfaces::srv::ManipService_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::ManipService>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::ManipService_Request>::value &&
    has_bounded_size<interfaces::srv::ManipService_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::ManipService>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::ManipService_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::ManipService_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__MANIP_SERVICE__TRAITS_HPP_
