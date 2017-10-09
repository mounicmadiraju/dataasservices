extern crate byteorder;
use std::io::Read;
use std::io::Write;
use std::collections::HashMap;
use byteorder::{ReadBytesExt, WriteBytesExt, BigEndian};


fn as_aligned(i: u16) -> u16 {
    let remainder = i % 4;
    if remainder == 0 {
        i
    } else {
        4 - remainder
    }
}

pub fn encode(hm: &HashMap<u16, String>) -> Vec<u8> {
    // each entry has at least 2 bytes
    let vec = Vec::with_capacity(hm.len() * 2);
    let mut buf = std::io::BufWriter::new(vec);
    for (k, v) in hm.iter() {
        // unwrap is fine since we're writing to an in-memory vector
        buf.write_u16::<BigEndian>(*k).unwrap();
        let write_length = v.len() as u16;
        buf.write_u16::<BigEndian>(write_length).unwrap();
        buf.write(v.as_bytes()).unwrap();
        let align = as_aligned(write_length);
        if align != 0 {
            buf.write(vec![0; align as usize].as_slice()).unwrap();
        }
    };
    buf.into_inner().unwrap()
}

pub fn decode<T: std::io::BufRead>(mut buf: &mut T) -> Result<HashMap<u16, String>, std::io::Error> {
    let mut attrs = HashMap::new();
    while let Ok(attr_type) = buf.read_u16::<BigEndian>() {
        let length = try!(buf.read_u16::<BigEndian>());
        let align = as_aligned(length);
        {
            let mut value_rdr = buf.take(length as u64);
            let mut value_vec = &mut Vec::with_capacity(length as usize);
            try!(value_rdr.read_to_end(value_vec));
            attrs.insert(attr_type, String::from_utf8(value_vec.to_owned()).expect("Invalid UTF8"));
        };
        buf.consume(align as usize);
    }
    Ok(attrs)
}


#[cfg(test)]
mod tests {

    use super::*;
    use std::io::Cursor;
    use std::collections::HashMap;

    #[test]
    fn test_decode_tlv() {
        let attrs_raw = vec![0, 6, 0, 5, 72, 101, 108, 108, 111, 0, 0, 0, 0, 6, 0, 5, 72, 101, 108, 108, 111, 0, 0, 0];
        let rdr = &mut Cursor::new(attrs_raw);
        match decode(rdr) {
            Ok(m) => {
                assert_eq!(m.len(), 1);
                match m.get(&6) {
                    Some(v) => assert_eq!(v.to_string(), "Hello".to_string()),
                    None => unreachable!("Decoding did not return the correct data!")
                }
            },
            Err(err) =>
                unreachable!("Decoding did not return the correct data!")
        }
    }

    #[test]
    fn test_encode_tlv() {
        let attrs_raw = vec![0, 6, 0, 5, 72, 101, 108, 108, 111, 0, 0, 0];
        let mut hm = HashMap::new();
        hm.insert(6 as u16, "Hello".to_string());
        assert_eq!(encode(&hm), attrs_raw);
    }

    #[test]
    fn test_encode_decode_tlv() {
        let mut hm = HashMap::new();
        hm.insert(6 as u16, "Hello".to_string());
        let encoded = &mut Cursor::new(encode(&hm));
        assert_eq!(hm, decode(encoded).unwrap());
    }
}
