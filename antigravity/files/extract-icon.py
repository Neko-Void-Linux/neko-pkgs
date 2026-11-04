import sys, struct, json

asar_path, out_path = sys.argv[1], sys.argv[2]


def try_extract(json_offset):
    try:
        with open(asar_path, "rb") as f:
            head = f.read(16)
            if len(head) < 16:
                return False
            header_size = struct.unpack("<I", head[4:8])[0]
            if header_size == 0 or header_size > 10485760:
                return False
            json_size = struct.unpack("<I", head[json_offset-4:json_offset])[0]
            if not (4 < json_size < header_size):
                return False
            f.seek(json_offset)
            header = json.loads(f.read(json_size).decode("utf-8"))
            entry = header.get("files", {}).get("icon.png")
            if not entry:
                return False
            offset = int(entry["offset"])
            size = int(entry["size"])
            f.seek(8 + header_size + offset)
            data = f.read(size)
            if len(data) != size or data[:4] != b"\x89PNG":
                return False
            with open(out_path, "wb") as out:
                out.write(data)
            return True
    except Exception:
        return False


for off in (12, 16):
    if try_extract(off):
        sys.exit(0)
sys.exit(1)
