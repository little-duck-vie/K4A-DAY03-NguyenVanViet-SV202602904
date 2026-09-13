# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Nguyễn Văn Việt]
> **Mã Sinh Viên / Mã Học viên:** [2A202602904]
> **Chủ đề Lựa chọn:** [Trợ lý tư vấn mua bất động sản.]

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá             | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                            |
| :--------------------------------- | :---------------: | :------------------------------------------------------------------------------------ |
| **1. Multi-step Reasoning**  |       5/ 5       | Trợ lý tư vấn mua bất động sản phải phân tích nhu cầu người mua theo nhiều bước: xác định ngân sách, khu vực, số phòng ngủ, diện tích, pháp lý, trạng thái giao dịch, khả năng di chuyển và mức độ phù hợp. Với các yêu cầu phức tạp như "căn hộ 2 phòng ngủ dưới 3,5 tỷ tại Hà Nội, đi đến Cầu Giấy dưới 30 phút", Agent cần lọc dữ liệu, so sánh nhiều lựa chọn, xếp hạng phương án và đưa ra khuyến nghị cuối cùng. |
| **2. Tool Interaction**      |       5/ 5       | Chủ đề này phụ thuộc mạnh vào công cụ và dữ liệu bên ngoài, đặc biệt là MCP Server hoặc cơ sở dữ liệu bất động sản để tra cứu danh sách căn hộ, giá bán, vị trí, pháp lý, trạng thái còn bán/đã cọc và đặt lịch xem nhà. Nếu chỉ dùng chatbot trả lời văn bản, hệ thống không thể đảm bảo thông tin bất động sản cập nhật và không thể thực hiện hành động như tìm kiếm hoặc đặt lịch. |
| **3. Dynamic Decision**      |       3/ 5       | Bước xử lý tiếp theo có phụ thuộc vào kết quả quan sát từ Tool, ví dụ nếu tìm thấy nhiều căn phù hợp thì Agent cần so sánh và chọn căn tốt nhất, còn nếu không tìm thấy mã bất động sản thì phải báo không có dữ liệu. Tuy nhiên phạm vi quyết định vẫn tương đối có kiểm soát, chủ yếu xoay quanh lọc, so sánh, tư vấn và đặt lịch, chưa cần lập kế hoạch tự trị dài hoặc thay đổi chiến lược quá phức tạp. |
| **4. Long Horizon Goal**     |       5/ 5       | Quá trình tư vấn mua nhà thường kéo dài qua nhiều lượt hội thoại: người dùng có thể điều chỉnh ngân sách, đổi khu vực, hỏi thêm về pháp lý, so sánh các căn, chọn phương án và đặt lịch xem nhà. Agent cần duy trì mục tiêu xuyên suốt là tìm bất động sản phù hợp nhất với nhu cầu ban đầu, đồng thời ghi nhớ các ràng buộc đã nêu để không tư vấn lệch khỏi tiêu chí của người mua. |
| **TỔNG ĐIỂM AGENTIC FIT** | **18/ 20** | Với tổng điểm 18/20, bài toán "Trợ lý tư vấn mua bất động sản" rất phù hợp để triển khai Agentic System vì cần suy luận nhiều bước, gọi Tool qua MCP Server, xử lý kết quả động và duy trì mục tiêu tư vấn xuyên suốt nhiều lượt tương tác. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "tư vấn cho tôi nhà ở Hà Nội",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "property_search",
    "arguments": {
      "location": "Hà Nội"
    },
    "observation": {
      "status": "SUCCESS",
      "total": 25,
      "data": [
        {
          "property_id": "BDS001",
          "title": "Căn hộ 2PN tại Cầu Giấy",
          "location": "Cầu Giấy, Hà Nội",
          "price": 3.2,
          "bedrooms": 2,
          "area": 70,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS002",
          "title": "Căn hộ 2PN tại Nam Từ Liêm",
          "location": "Nam Từ Liêm, Hà Nội",
          "price": 2.9,
          "bedrooms": 2,
          "area": 68,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS003",
          "title": "Căn hộ 3PN tại Thanh Xuân",
          "location": "Thanh Xuân, Hà Nội",
          "price": 4.1,
          "bedrooms": 3,
          "area": 90,
          "legal_status": "Đang cập nhật",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS004",
          "title": "Studio gần Đại học Quốc gia",
          "location": "Cầu Giấy, Hà Nội",
          "price": 1.8,
          "bedrooms": 1,
          "area": 42,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS005",
          "title": "Căn hộ 2PN tại Mỹ Đình",
          "location": "Nam Từ Liêm, Hà Nội",
          "price": 3.4,
          "bedrooms": 2,
          "area": 75,
          "legal_status": "Hợp đồng mua bán",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS006",
          "title": "Căn hộ 1PN tại Tây Mỗ",
          "location": "Nam Từ Liêm, Hà Nội",
          "price": 2.1,
          "bedrooms": 1,
          "area": 48,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS007",
          "title": "Căn hộ 2PN gần Royal City",
          "location": "Thanh Xuân, Hà Nội",
          "price": 3.6,
          "bedrooms": 2,
          "area": 72,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS008",
          "title": "Căn hộ 2PN tại Linh Đàm",
          "location": "Hoàng Mai, Hà Nội",
          "price": 2.4,
          "bedrooms": 2,
          "area": 65,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS009",
          "title": "Căn hộ 3PN view hồ Linh Đàm",
          "location": "Hoàng Mai, Hà Nội",
          "price": 3.7,
          "bedrooms": 3,
          "area": 92,
          "legal_status": "Đang cập nhật",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS010",
          "title": "Căn hộ 2PN tại Long Biên",
          "location": "Long Biên, Hà Nội",
          "price": 2.8,
          "bedrooms": 2,
          "area": 69,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS011",
          "title": "Căn hộ 3PN tại Vinhomes Riverside",
          "location": "Long Biên, Hà Nội",
          "price": 5.2,
          "bedrooms": 3,
          "area": 105,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS012",
          "title": "Nhà phố 4 tầng tại Hà Đông",
          "location": "Hà Đông, Hà Nội",
          "price": 6.8,
          "bedrooms": 4,
          "area": 58,
          "legal_status": "Sổ đỏ",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS013",
          "title": "Căn hộ 2PN tại Văn Quán",
          "location": "Hà Đông, Hà Nội",
          "price": 2.6,
          "bedrooms": 2,
          "area": 67,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS014",
          "title": "Căn hộ 1PN tại Dương Nội",
          "location": "Hà Đông, Hà Nội",
          "price": 1.9,
          "bedrooms": 1,
          "area": 45,
          "legal_status": "Hợp đồng mua bán",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS015",
          "title": "Căn hộ 2PN tại Times City",
          "location": "Hai Bà Trưng, Hà Nội",
          "price": 4.3,
          "bedrooms": 2,
          "area": 78,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS016",
          "title": "Căn hộ 3PN tại Minh Khai",
          "location": "Hai Bà Trưng, Hà Nội",
          "price": 4.9,
          "bedrooms": 3,
          "area": 96,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS017",
          "title": "Căn hộ 2PN tại Tây Hồ",
          "location": "Tây Hồ, Hà Nội",
          "price": 5.5,
          "bedrooms": 2,
          "area": 82,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS018",
          "title": "Căn hộ 3PN view Hồ Tây",
          "location": "Tây Hồ, Hà Nội",
          "price": 8.9,
          "bedrooms": 3,
          "area": 120,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS019",
          "title": "Nhà riêng ngõ ô tô tại Ba Đình",
          "location": "Ba Đình, Hà Nội",
          "price": 9.5,
          "bedrooms": 4,
          "area": 62,
          "legal_status": "Sổ đỏ",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS020",
          "title": "Căn hộ 2PN tại Giảng Võ",
          "location": "Ba Đình, Hà Nội",
          "price": 4.6,
          "bedrooms": 2,
          "area": 74,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS021",
          "title": "Căn hộ 2PN tại Đống Đa",
          "location": "Đống Đa, Hà Nội",
          "price": 3.8,
          "bedrooms": 2,
          "area": 71,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS022",
          "title": "Nhà tập thể cải tạo tại Kim Liên",
          "location": "Đống Đa, Hà Nội",
          "price": 2.2,
          "bedrooms": 2,
          "area": 55,
          "legal_status": "Sổ đỏ",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS023",
          "title": "Căn hộ 2PN tại Ciputra",
          "location": "Bắc Từ Liêm, Hà Nội",
          "price": 4.2,
          "bedrooms": 2,
          "area": 80,
          "legal_status": "Sổ hồng",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS024",
          "title": "Căn hộ 3PN tại Ngoại Giao Đoàn",
          "location": "Bắc Từ Liêm, Hà Nội",
          "price": 5.1,
          "bedrooms": 3,
          "area": 102,
          "legal_status": "Hợp đồng mua bán",
          "status": "Đang bán"
        },
        {
          "property_id": "BDS025",
          "title": "Căn hộ 2PN tại Xuân Đỉnh",
          "location": "Bắc Từ Liêm, Hà Nội",
          "price": 3.1,
          "bedrooms": 2,
          "area": 70,
          "legal_status": "Sổ hồng",
          "status": "Đã cọc"
        }
      ]
    },
    "latency_ms": 3678.48
  },
  {
    "step": 2,
    "query": "tư vấn cho tôi nhà ở Hà Nội",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Tìm thấy 25 bất động sản phù hợp:\n- BDS001: Căn hộ 2PN tại Cầu Giấy | Vị trí: Cầu Giấy, Hà Nội | Giá: 3.2 tỷ VNĐ | 2 phòng ngủ | Diện tích: 70 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS002: Căn hộ 2PN tại Nam Từ Liêm | Vị trí: Nam Từ Liêm, Hà Nội | Giá: 2.9 tỷ VNĐ | 2 phòng ngủ | Diện tích: 68 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS003: Căn hộ 3PN tại Thanh Xuân | Vị trí: Thanh Xuân, Hà Nội | Giá: 4.1 tỷ VNĐ | 3 phòng ngủ | Diện tích: 90 m2 | Pháp lý: Đang cập nhật | Trạng thái: Đang bán\n- BDS004: Studio gần Đại học Quốc gia | Vị trí: Cầu Giấy, Hà Nội | Giá: 1.8 tỷ VNĐ | 1 phòng ngủ | Diện tích: 42 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS005: Căn hộ 2PN tại Mỹ Đình | Vị trí: Nam Từ Liêm, Hà Nội | Giá: 3.4 tỷ VNĐ | 2 phòng ngủ | Diện tích: 75 m2 | Pháp lý: Hợp đồng mua bán | Trạng thái: Đang bán\n- BDS006: Căn hộ 1PN tại Tây Mỗ | Vị trí: Nam Từ Liêm, Hà Nội | Giá: 2.1 tỷ VNĐ | 1 phòng ngủ | Diện tích: 48 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS007: Căn hộ 2PN gần Royal City | Vị trí: Thanh Xuân, Hà Nội | Giá: 3.6 tỷ VNĐ | 2 phòng ngủ | Diện tích: 72 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS008: Căn hộ 2PN tại Linh Đàm | Vị trí: Hoàng Mai, Hà Nội | Giá: 2.4 tỷ VNĐ | 2 phòng ngủ | Diện tích: 65 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS009: Căn hộ 3PN view hồ Linh Đàm | Vị trí: Hoàng Mai, Hà Nội | Giá: 3.7 tỷ VNĐ | 3 phòng ngủ | Diện tích: 92 m2 | Pháp lý: Đang cập nhật | Trạng thái: Đang bán\n- BDS010: Căn hộ 2PN tại Long Biên | Vị trí: Long Biên, Hà Nội | Giá: 2.8 tỷ VNĐ | 2 phòng ngủ | Diện tích: 69 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS011: Căn hộ 3PN tại Vinhomes Riverside | Vị trí: Long Biên, Hà Nội | Giá: 5.2 tỷ VNĐ | 3 phòng ngủ | Diện tích: 105 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS012: Nhà phố 4 tầng tại Hà Đông | Vị trí: Hà Đông, Hà Nội | Giá: 6.8 tỷ VNĐ | 4 phòng ngủ | Diện tích: 58 m2 | Pháp lý: Sổ đỏ | Trạng thái: Đang bán\n- BDS013: Căn hộ 2PN tại Văn Quán | Vị trí: Hà Đông, Hà Nội | Giá: 2.6 tỷ VNĐ | 2 phòng ngủ | Diện tích: 67 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS014: Căn hộ 1PN tại Dương Nội | Vị trí: Hà Đông, Hà Nội | Giá: 1.9 tỷ VNĐ | 1 phòng ngủ | Diện tích: 45 m2 | Pháp lý: Hợp đồng mua bán | Trạng thái: Đang bán\n- BDS015: Căn hộ 2PN tại Times City | Vị trí: Hai Bà Trưng, Hà Nội | Giá: 4.3 tỷ VNĐ | 2 phòng ngủ | Diện tích: 78 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS016: Căn hộ 3PN tại Minh Khai | Vị trí: Hai Bà Trưng, Hà Nội | Giá: 4.9 tỷ VNĐ | 3 phòng ngủ | Diện tích: 96 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS017: Căn hộ 2PN tại Tây Hồ | Vị trí: Tây Hồ, Hà Nội | Giá: 5.5 tỷ VNĐ | 2 phòng ngủ | Diện tích: 82 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS018: Căn hộ 3PN view Hồ Tây | Vị trí: Tây Hồ, Hà Nội | Giá: 8.9 tỷ VNĐ | 3 phòng ngủ | Diện tích: 120 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS019: Nhà riêng ngõ ô tô tại Ba Đình | Vị trí: Ba Đình, Hà Nội | Giá: 9.5 tỷ VNĐ | 4 phòng ngủ | Diện tích: 62 m2 | Pháp lý: Sổ đỏ | Trạng thái: Đang bán\n- BDS020: Căn hộ 2PN tại Giảng Võ | Vị trí: Ba Đình, Hà Nội | Giá: 4.6 tỷ VNĐ | 2 phòng ngủ | Diện tích: 74 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS021: Căn hộ 2PN tại Đống Đa | Vị trí: Đống Đa, Hà Nội | Giá: 3.8 tỷ VNĐ | 2 phòng ngủ | Diện tích: 71 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS022: Nhà tập thể cải tạo tại Kim Liên | Vị trí: Đống Đa, Hà Nội | Giá: 2.2 tỷ VNĐ | 2 phòng ngủ | Diện tích: 55 m2 | Pháp lý: Sổ đỏ | Trạng thái: Đang bán\n- BDS023: Căn hộ 2PN tại Ciputra | Vị trí: Bắc Từ Liêm, Hà Nội | Giá: 4.2 tỷ VNĐ | 2 phòng ngủ | Diện tích: 80 m2 | Pháp lý: Sổ hồng | Trạng thái: Đang bán\n- BDS024: Căn hộ 3PN tại Ngoại Giao Đoàn | Vị trí: Bắc Từ Liêm, Hà Nội | Giá: 5.1 tỷ VNĐ | 3 phòng ngủ | Diện tích: 102 m2 | Pháp lý: Hợp đồng mua bán | Trạng thái: Đang bán\n- BDS025: Căn hộ 2PN tại Xuân Đỉnh | Vị trí: Bắc Từ Liêm, Hà Nội | Giá: 3.1 tỷ VNĐ | 2 phòng ngủ | Diện tích: 70 m2 | Pháp lý: Sổ hồng | Trạng thái: Đã cọc",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [X] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).

- **Tổng số Test Cases đã chạy thành công:** __5_ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** _5__ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
