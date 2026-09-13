"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
  {
    "name": "property_search",
    "description": "Tìm kiếm bất động sản theo khu vực, ngân sách và số phòng ngủ.",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "Khu vực cần tìm, ví dụ Cầu Giấy, Hà Nội."
        },
        "max_price": {
          "type": "number",
          "description": "Giá tối đa, đơn vị tỷ VNĐ."
        },
        "bedrooms": {
          "type": "integer",
          "description": "Số phòng ngủ mong muốn."
        }
      },
      "required": ["location"]
    }
  },
  {
    "name": "property_detail",
    "description": "Tra cứu thông tin chi tiết của một bất động sản theo mã.",
    "parameters": {
      "type": "object",
      "properties": {
        "property_id": {
          "type": "string",
          "description": "Mã bất động sản, ví dụ BDS001."
        }
      },
      "required": ["property_id"]
    }
  },
  {
    "name": "calculate_travel_time",
    "description": "Tính thời gian di chuyển từ bất động sản đến địa điểm người dùng quan tâm.",
    "parameters": {
      "type": "object",
      "properties": {
        "property_id": {
          "type": "string",
          "description": "Mã bất động sản."
        },
        "destination": {
          "type": "string",
          "description": "Địa điểm đích, ví dụ Cầu Giấy."
        }
      },
      "required": ["property_id", "destination"]
    }
  },
  {
    "name": "schedule_property_viewing",
    "description": "Đặt lịch xem bất động sản.",
    "parameters": {
      "type": "object",
      "properties": {
        "property_id": {
          "type": "string",
          "description": "Mã bất động sản muốn xem."
        },
        "appointment_time": {
          "type": "string",
          "description": "Thời gian đặt lịch, ví dụ 2026-09-20T14:00:00+07:00."
        }
      },
      "required": ["property_id", "appointment_time"]
    }
  }
]

# ------------------------------------------------------------------------------
# MOCK DATABASE
# ------------------------------------------------------------------------------

MOCK_DATABASE = {
    "BDS001": {
        "title": "Căn hộ 2PN tại Cầu Giấy",
        "location": "Cầu Giấy, Hà Nội",
        "price": 3.2,
        "bedrooms": 2,
        "area": 70,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS002": {
        "title": "Căn hộ 2PN tại Nam Từ Liêm",
        "location": "Nam Từ Liêm, Hà Nội",
        "price": 2.9,
        "bedrooms": 2,
        "area": 68,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS003": {
        "title": "Căn hộ 3PN tại Thanh Xuân",
        "location": "Thanh Xuân, Hà Nội",
        "price": 4.1,
        "bedrooms": 3,
        "area": 90,
        "legal_status": "Đang cập nhật",
        "status": "Đang bán"
    },
    "BDS004": {
        "title": "Studio gần Đại học Quốc gia",
        "location": "Cầu Giấy, Hà Nội",
        "price": 1.8,
        "bedrooms": 1,
        "area": 42,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS005": {
        "title": "Căn hộ 2PN tại Mỹ Đình",
        "location": "Nam Từ Liêm, Hà Nội",
        "price": 3.4,
        "bedrooms": 2,
        "area": 75,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS006": {
        "title": "Căn hộ 1PN tại Tây Mỗ",
        "location": "Nam Từ Liêm, Hà Nội",
        "price": 2.1,
        "bedrooms": 1,
        "area": 48,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS007": {
        "title": "Căn hộ 2PN gần Royal City",
        "location": "Thanh Xuân, Hà Nội",
        "price": 3.6,
        "bedrooms": 2,
        "area": 72,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS008": {
        "title": "Căn hộ 2PN tại Linh Đàm",
        "location": "Hoàng Mai, Hà Nội",
        "price": 2.4,
        "bedrooms": 2,
        "area": 65,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS009": {
        "title": "Căn hộ 3PN view hồ Linh Đàm",
        "location": "Hoàng Mai, Hà Nội",
        "price": 3.7,
        "bedrooms": 3,
        "area": 92,
        "legal_status": "Đang cập nhật",
        "status": "Đang bán"
    },
    "BDS010": {
        "title": "Căn hộ 2PN tại Long Biên",
        "location": "Long Biên, Hà Nội",
        "price": 2.8,
        "bedrooms": 2,
        "area": 69,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS011": {
        "title": "Căn hộ 3PN tại Vinhomes Riverside",
        "location": "Long Biên, Hà Nội",
        "price": 5.2,
        "bedrooms": 3,
        "area": 105,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS012": {
        "title": "Nhà phố 4 tầng tại Hà Đông",
        "location": "Hà Đông, Hà Nội",
        "price": 6.8,
        "bedrooms": 4,
        "area": 58,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS013": {
        "title": "Căn hộ 2PN tại Văn Quán",
        "location": "Hà Đông, Hà Nội",
        "price": 2.6,
        "bedrooms": 2,
        "area": 67,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS014": {
        "title": "Căn hộ 1PN tại Dương Nội",
        "location": "Hà Đông, Hà Nội",
        "price": 1.9,
        "bedrooms": 1,
        "area": 45,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS015": {
        "title": "Căn hộ 2PN tại Times City",
        "location": "Hai Bà Trưng, Hà Nội",
        "price": 4.3,
        "bedrooms": 2,
        "area": 78,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS016": {
        "title": "Căn hộ 3PN tại Minh Khai",
        "location": "Hai Bà Trưng, Hà Nội",
        "price": 4.9,
        "bedrooms": 3,
        "area": 96,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS017": {
        "title": "Căn hộ 2PN tại Tây Hồ",
        "location": "Tây Hồ, Hà Nội",
        "price": 5.5,
        "bedrooms": 2,
        "area": 82,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS018": {
        "title": "Căn hộ 3PN view Hồ Tây",
        "location": "Tây Hồ, Hà Nội",
        "price": 8.9,
        "bedrooms": 3,
        "area": 120,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS019": {
        "title": "Nhà riêng ngõ ô tô tại Ba Đình",
        "location": "Ba Đình, Hà Nội",
        "price": 9.5,
        "bedrooms": 4,
        "area": 62,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS020": {
        "title": "Căn hộ 2PN tại Giảng Võ",
        "location": "Ba Đình, Hà Nội",
        "price": 4.6,
        "bedrooms": 2,
        "area": 74,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS021": {
        "title": "Căn hộ 2PN tại Đống Đa",
        "location": "Đống Đa, Hà Nội",
        "price": 3.8,
        "bedrooms": 2,
        "area": 71,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS022": {
        "title": "Nhà tập thể cải tạo tại Kim Liên",
        "location": "Đống Đa, Hà Nội",
        "price": 2.2,
        "bedrooms": 2,
        "area": 55,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS023": {
        "title": "Căn hộ 2PN tại Ciputra",
        "location": "Bắc Từ Liêm, Hà Nội",
        "price": 4.2,
        "bedrooms": 2,
        "area": 80,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS024": {
        "title": "Căn hộ 3PN tại Ngoại Giao Đoàn",
        "location": "Bắc Từ Liêm, Hà Nội",
        "price": 5.1,
        "bedrooms": 3,
        "area": 102,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS025": {
        "title": "Căn hộ 2PN tại Xuân Đỉnh",
        "location": "Bắc Từ Liêm, Hà Nội",
        "price": 3.1,
        "bedrooms": 2,
        "area": 70,
        "legal_status": "Sổ hồng",
        "status": "Đã cọc"
    },
    "BDS026": {
        "title": "Căn hộ 2PN tại Phú Nhuận",
        "location": "Phú Nhuận, TP.HCM",
        "price": 4.4,
        "bedrooms": 2,
        "area": 73,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS027": {
        "title": "Căn hộ 1PN tại Bình Thạnh",
        "location": "Bình Thạnh, TP.HCM",
        "price": 2.7,
        "bedrooms": 1,
        "area": 50,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS028": {
        "title": "Căn hộ 2PN gần Landmark 81",
        "location": "Bình Thạnh, TP.HCM",
        "price": 5.8,
        "bedrooms": 2,
        "area": 79,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS029": {
        "title": "Căn hộ 3PN tại Thủ Đức",
        "location": "Thủ Đức, TP.HCM",
        "price": 4.0,
        "bedrooms": 3,
        "area": 95,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS030": {
        "title": "Căn hộ 2PN tại An Phú",
        "location": "Thủ Đức, TP.HCM",
        "price": 3.5,
        "bedrooms": 2,
        "area": 72,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS031": {
        "title": "Nhà phố tại Quận 7",
        "location": "Quận 7, TP.HCM",
        "price": 8.2,
        "bedrooms": 4,
        "area": 80,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS032": {
        "title": "Căn hộ 2PN tại Phú Mỹ Hưng",
        "location": "Quận 7, TP.HCM",
        "price": 4.9,
        "bedrooms": 2,
        "area": 82,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS033": {
        "title": "Căn hộ 1PN tại Tân Bình",
        "location": "Tân Bình, TP.HCM",
        "price": 2.3,
        "bedrooms": 1,
        "area": 46,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS034": {
        "title": "Căn hộ 2PN gần sân bay Tân Sơn Nhất",
        "location": "Tân Bình, TP.HCM",
        "price": 3.6,
        "bedrooms": 2,
        "area": 69,
        "legal_status": "Đang cập nhật",
        "status": "Đang bán"
    },
    "BDS035": {
        "title": "Căn hộ 2PN tại Gò Vấp",
        "location": "Gò Vấp, TP.HCM",
        "price": 2.9,
        "bedrooms": 2,
        "area": 66,
        "legal_status": "Sổ hồng",
        "status": "Đã cọc"
    },
    "BDS036": {
        "title": "Nhà riêng 3 tầng tại Gò Vấp",
        "location": "Gò Vấp, TP.HCM",
        "price": 5.7,
        "bedrooms": 3,
        "area": 60,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS037": {
        "title": "Căn hộ 2PN tại Hải Châu",
        "location": "Hải Châu, Đà Nẵng",
        "price": 3.0,
        "bedrooms": 2,
        "area": 68,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS038": {
        "title": "Căn hộ biển Mỹ Khê 1PN",
        "location": "Sơn Trà, Đà Nẵng",
        "price": 2.5,
        "bedrooms": 1,
        "area": 52,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS039": {
        "title": "Căn hộ 3PN view sông Hàn",
        "location": "Sơn Trà, Đà Nẵng",
        "price": 5.0,
        "bedrooms": 3,
        "area": 110,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS040": {
        "title": "Nhà phố tại Cẩm Lệ",
        "location": "Cẩm Lệ, Đà Nẵng",
        "price": 4.1,
        "bedrooms": 3,
        "area": 75,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS041": {
        "title": "Căn hộ 2PN tại Nha Trang Center",
        "location": "Nha Trang, Khánh Hòa",
        "price": 3.3,
        "bedrooms": 2,
        "area": 70,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS042": {
        "title": "Căn hộ nghỉ dưỡng Bãi Dài",
        "location": "Cam Ranh, Khánh Hòa",
        "price": 2.8,
        "bedrooms": 1,
        "area": 55,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS043": {
        "title": "Biệt thự biển Cam Ranh",
        "location": "Cam Ranh, Khánh Hòa",
        "price": 12.5,
        "bedrooms": 4,
        "area": 240,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS044": {
        "title": "Căn hộ 2PN trung tâm Hạ Long",
        "location": "Hạ Long, Quảng Ninh",
        "price": 2.7,
        "bedrooms": 2,
        "area": 64,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS045": {
        "title": "Shophouse Bãi Cháy",
        "location": "Hạ Long, Quảng Ninh",
        "price": 9.8,
        "bedrooms": 4,
        "area": 120,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS046": {
        "title": "Căn hộ 2PN tại Dĩ An",
        "location": "Dĩ An, Bình Dương",
        "price": 1.9,
        "bedrooms": 2,
        "area": 60,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS047": {
        "title": "Căn hộ 3PN tại Thuận An",
        "location": "Thuận An, Bình Dương",
        "price": 2.6,
        "bedrooms": 3,
        "area": 86,
        "legal_status": "Hợp đồng mua bán",
        "status": "Đang bán"
    },
    "BDS048": {
        "title": "Nhà phố khu đô thị Mỹ Phước",
        "location": "Bến Cát, Bình Dương",
        "price": 3.2,
        "bedrooms": 3,
        "area": 100,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    },
    "BDS049": {
        "title": "Căn hộ 2PN tại Biên Hòa",
        "location": "Biên Hòa, Đồng Nai",
        "price": 2.2,
        "bedrooms": 2,
        "area": 62,
        "legal_status": "Sổ hồng",
        "status": "Đang bán"
    },
    "BDS050": {
        "title": "Nhà vườn ven sông Long Thành",
        "location": "Long Thành, Đồng Nai",
        "price": 6.5,
        "bedrooms": 3,
        "area": 300,
        "legal_status": "Sổ đỏ",
        "status": "Đang bán"
    }
}


# ------------------------------------------------------------------------------
# TOOL 1: SEARCH PROPERTY
# ------------------------------------------------------------------------------

def execute_property_search(
    location: str,
    max_price: float = None,
    bedrooms: int = None
) -> str:
    """
    Tìm bất động sản theo khu vực, giá tối đa và số phòng ngủ.
    """

    results = []

    for property_id, property_data in MOCK_DATABASE.items():

        # Kiểm tra khu vực
        if location.lower() not in property_data["location"].lower():
            continue

        # Kiểm tra giá
        if max_price is not None and property_data["price"] > max_price:
            continue

        # Kiểm tra số phòng ngủ
        if bedrooms is not None and property_data["bedrooms"] != bedrooms:
            continue

        results.append({
            "property_id": property_id,
            **property_data
        })

    if results:
        return json.dumps({
            "status": "SUCCESS",
            "total": len(results),
            "data": results
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": "Không tìm thấy bất động sản phù hợp với yêu cầu."
    }, ensure_ascii=False)


# ------------------------------------------------------------------------------
# TOOL 2: PROPERTY DETAIL
# ------------------------------------------------------------------------------

def execute_property_detail(property_id: str) -> str:
    """
    Tra cứu chi tiết bất động sản theo mã.
    """

    property_id = property_id.strip().upper()

    property_data = MOCK_DATABASE.get(property_id)

    if property_data:
        return json.dumps({
            "status": "SUCCESS",
            "property_id": property_id,
            "data": property_data
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy bất động sản có mã '{property_id}'."
    }, ensure_ascii=False)


# ------------------------------------------------------------------------------
# TOOL 3: CALCULATE TRAVEL TIME
# ------------------------------------------------------------------------------

def execute_calculate_travel_time(
    property_id: str,
    destination: str
) -> str:
    """
    Mô phỏng thời gian di chuyển từ bất động sản tới địa điểm đích.
    """

    property_id = property_id.strip().upper()

    property_data = MOCK_DATABASE.get(property_id)

    if not property_data:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy bất động sản có mã '{property_id}'."
        }, ensure_ascii=False)

    # Mock thời gian di chuyển
    MOCK_TRAVEL_TIME = {
        "BDS001": 15,
        "BDS002": 25,
        "BDS003": 20
    }

    travel_time = MOCK_TRAVEL_TIME.get(property_id, 30)

    return json.dumps({
        "status": "SUCCESS",
        "property_id": property_id,
        "from": property_data["location"],
        "destination": destination,
        "travel_time_minutes": travel_time,
        "message": (
            f"Thời gian di chuyển ước tính từ "
            f"{property_data['location']} đến {destination} "
            f"là khoảng {travel_time} phút."
        )
    }, ensure_ascii=False)


# ------------------------------------------------------------------------------
# TOOL 4: SCHEDULE PROPERTY VIEWING
# ------------------------------------------------------------------------------

def execute_schedule_property_viewing(
    property_id: str,
    appointment_time: str
) -> str:
    """
    Đặt lịch xem bất động sản.
    """

    property_id = property_id.strip().upper()

    property_data = MOCK_DATABASE.get(property_id)

    if not property_data:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy bất động sản có mã '{property_id}'."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"VIEW-{property_id}-99",
        "property_id": property_id,
        "property": property_data["title"],
        "appointment_time": appointment_time,
        "message": (
            f"Đặt lịch xem {property_id} thành công "
            f"vào lúc {appointment_time}."
        )
    }, ensure_ascii=False)


# ==============================================================================
# TOOL ROUTER
# ==============================================================================

TOOL_ROUTER = {
    "property_search": execute_property_search,
    "property_detail": execute_property_detail,
    "calculate_travel_time": execute_calculate_travel_time,
    "schedule_property_viewing": execute_schedule_property_viewing
}


def dispatch_tool_call(
    tool_name: str,
    arguments: Dict[str, Any]
) -> str:
    """
    Hàm trung chuyển để Agent gọi tool thực tế.
    """

    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)

        except Exception as e:
            return json.dumps({
                "status": "EXECUTION_ERROR",
                "error": str(e)
            }, ensure_ascii=False)

    return json.dumps({
        "status": "UNKNOWN_TOOL",
        "error": f"Tool '{tool_name}' không tồn tại!"
    }, ensure_ascii=False)
