use std::collections::HashMap;
use std::io::Cursor;
use messageattribute::MessageAttribute;
use method::{Method};
//use class::{Class};
use tlv;

pub const STUN_PACKET_SIZE: usize = 576;
pub const STUN_HEADER_SIZE: usize = 20;
pub const STUN_MAGIC_COOKIE: u32 = 0x2112A442;

pub struct Header {
    data: Vec<u8>,
}

impl Header {
    pub fn new_from_vec(data: Vec<u8>) -> Header {
        // TODO: Implement parsing here. Fill fields with set_*
        // functions and return a struct with values instead of
        // holding onto the vector.

        Header { data: data }
    }

    pub fn new(data: Vec<u8>) -> Header {
        Header { data: data }
    }

    pub fn set_transaction_id(&mut self, value: [u16; 8usize]) {
        {
            {
                let value = value[0usize];
                {
                    self.data[8usize] = (self.data[8usize] & !255u8) |
                                        ((value >> 4usize) as u8) & 255u8;
                    self.data[9usize] = (self.data[9usize] & !240u8) |
                                        ((value << 4usize) as u8) & 240u8;
                };
            }
            {
                let value = value[1usize];
                {
                    self.data[9usize] = (self.data[9usize] & !15u8) |
                                        ((value >> 8usize) as u8) & 15u8;
                    self.data[10usize] = (self.data[10usize] & !255u8) |
                                         ((value << 0usize) as u8) & 255u8;
                };
            }
            {
                let value = value[2usize];
                {
                    self.data[11usize] = (self.data[11usize] & !255u8) |
                                         ((value >> 4usize) as u8) & 255u8;
                    self.data[12usize] = (self.data[12usize] & !240u8) |
                                         ((value << 4usize) as u8) & 240u8;
                };
            }
            {
                let value = value[3usize];
                {
                    self.data[12usize] = (self.data[12usize] & !15u8) |
                                         ((value >> 8usize) as u8) & 15u8;
                    self.data[13usize] = (self.data[13usize] & !255u8) |
                                         ((value << 0usize) as u8) & 255u8;
                };
            }
            {
                let value = value[4usize];
                {
                    self.data[14usize] = (self.data[14usize] & !255u8) |
                                         ((value >> 4usize) as u8) & 255u8;
                    self.data[15usize] = (self.data[15usize] & !240u8) |
                                         ((value << 4usize) as u8) & 240u8;
                };
            }
            {
                let value = value[5usize];
                {
                    self.data[15usize] = (self.data[15usize] & !15u8) |
                                         ((value >> 8usize) as u8) & 15u8;
                    self.data[16usize] = (self.data[16usize] & !255u8) |
                                         ((value << 0usize) as u8) & 255u8;
                };
            }
            {
                let value = value[6usize];
                {
                    self.data[17usize] = (self.data[17usize] & !255u8) |
                                         ((value >> 4usize) as u8) & 255u8;
                    self.data[18usize] = (self.data[18usize] & !240u8) |
                                         ((value << 4usize) as u8) & 240u8;
                };
            }
            {
                let value = value[7usize];
                {
                    self.data[18usize] = (self.data[18usize] & !15u8) |
                                         ((value >> 8usize) as u8) & 15u8;
                    self.data[19usize] = (self.data[19usize] & !255u8) |
                                         ((value << 0usize) as u8) & 255u8;
                };
            }
        };
    }

    pub fn get_marker(&self) -> u8 {
        ((self.data[0usize] >> 6usize) & 3u8) as u8
    }

    pub fn set_marker(&mut self, value: u8) {
        {
            self.data[0usize] = (self.data[0usize] & !192u8) | ((value << 6usize) as u8) & 192u8;
        };
    }

    fn get_m0(&self) -> u8 {
        ((self.data[0usize] >> 1usize) & 31u8) as u8
    }

    fn set_m0(&mut self, value: u8) {
        {
            self.data[0usize] = (self.data[0usize] & !62u8) | ((value << 1usize) as u8) & 62u8;
        };
    }

    pub fn get_c0(&self) -> u8 {
        (self.data[(7u64 / 8) as usize] & (1 << 0usize))
    }

    pub fn set_c0(&mut self, value: u8) {
        if value == 1 {
            self.data[0usize] |= 1u8
        } else {
            self.data[0usize] &= !(1u8)
        }
    }

    fn get_m1(&self) -> u8 {
        ((self.data[1usize] >> 5usize) & 7u8) as u8
    }

    fn set_m1(&mut self, value: u8) {
        {
            self.data[1usize] = (self.data[1usize] & !224u8) | ((value << 5usize) as u8) & 224u8;
        };
    }

    fn get_c1(&self) -> bool {
        (self.data[(11u64 / 8) as usize] & (1 << 4usize)) != 0
    }

    pub fn set_c1(&mut self, value: bool) {
        if value {
            self.data[1usize] |= 16u8
        } else {
            self.data[1usize] &= !(16u8)
        }
    }

    fn get_m2(&self) -> u8 {
        ((self.data[1usize] >> 0usize) & 15u8) as u8
    }

    fn set_m2(&mut self, value: u8) {
        {
            self.data[1usize] = (self.data[1usize] & !15u8) | ((value << 0usize) as u8) & 15u8;
        };
    }

    pub fn get_length(&self) -> u16 {
        (((self.data[2usize] >> 0usize) & 255u8) as u16) << 8usize |
        (((self.data[3usize] >> 0usize) & 255u8) as u16)
    }

    pub fn set_length(&mut self, value: u16) {
        {
            self.data[2usize] = (self.data[2usize] & !255u8) | ((value >> 8usize) as u8) & 255u8;
            self.data[3usize] = (self.data[3usize] & !255u8) | ((value << 0usize) as u8) & 255u8;
        };
    }

    pub fn get_magic_cookie(&self) -> u32 {
        (((((self.data[4usize] >> 0usize) & 255u8) as u32) << 8usize |
          (((self.data[5usize] >> 0usize) & 255u8) as u32)) << 8usize |
         (((self.data[6usize] >> 0usize) & 255u8) as u32)) << 8usize |
        (((self.data[7usize] >> 0usize) & 255u8) as u32)
    }

    pub fn set_magic_cookie(&mut self, value: u32) {
        {
            self.data[4usize] = (self.data[4usize] & !255u8) | ((value >> 24usize) as u8) & 255u8;
            self.data[5usize] = (self.data[5usize] & !255u8) | ((value >> 16usize) as u8) & 255u8;
            self.data[6usize] = (self.data[6usize] & !255u8) | ((value >> 8usize) as u8) & 255u8;
            self.data[7usize] = (self.data[7usize] & !255u8) | ((value << 0usize) as u8) & 255u8;
        };
    }

    pub fn get_transaction_id(&self) -> [u16; 8usize] {
        [(((self.data[8usize] >> 0usize) & 255u8) as u16) << 4usize |
         (((self.data[9usize] >> 4usize) & 15u8) as u16),
         (((self.data[9usize] >> 0usize) & 15u8) as u16) << 8usize |
         (((self.data[10usize] >> 0usize) & 255u8) as u16),
         (((self.data[11usize] >> 0usize) & 255u8) as u16) << 4usize |
         (((self.data[12usize] >> 4usize) & 15u8) as u16),
         (((self.data[12usize] >> 0usize) & 15u8) as u16) << 8usize |
         (((self.data[13usize] >> 0usize) & 255u8) as u16),
         (((self.data[14usize] >> 0usize) & 255u8) as u16) << 4usize |
         (((self.data[15usize] >> 4usize) & 15u8) as u16),
         (((self.data[15usize] >> 0usize) & 15u8) as u16) << 8usize |
         (((self.data[16usize] >> 0usize) & 255u8) as u16),
         (((self.data[17usize] >> 0usize) & 255u8) as u16) << 4usize |
         (((self.data[18usize] >> 4usize) & 15u8) as u16),
         (((self.data[18usize] >> 0usize) & 15u8) as u16) << 8usize |
         (((self.data[19usize] >> 0usize) & 255u8) as u16)]
    }

    pub fn get_method(&self) -> Method {
        let m0 = (self.get_m0() << 7) as u16;
        let m1 = (self.get_m1() << 4) as u16;
        let m2 = self.get_m2() as u16;
        Method::from_u16(m0 | m1 | m2).unwrap()
    }

    pub fn set_method(&self, method: Method) {
        let method = method.to_u16();
        let m0 = method >> 7;
        let m1 = method >> 4 & 15;
        let m2 = method;
    }

    pub fn get_attributes(&self) -> HashMap<MessageAttribute, String> {
        let mut attrs = HashMap::new();
        if self.data.len() < STUN_HEADER_SIZE {
            return attrs;
        }
        let (_, attributes) = self.data.split_at(STUN_HEADER_SIZE);
        let mut attrs_vec = &mut Cursor::new(attributes.to_vec());
        let attrs_tlv = tlv::decode(attrs_vec).unwrap();
        for (k, v) in attrs_tlv.iter() {
            attrs.insert(MessageAttribute::from_u16(*k), v.to_owned());
        }
        attrs
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use method::{Method};

    #[test]
    fn decode_header() {
        let stun_header_raw = vec![0, 1, 0, 56, 33, 18, 164, 66, 183, 231, 167, 1, 188, 52, 214,
                                   134, 250, 135, 223, 174];
        let stun_header = Header::new(stun_header_raw);
        assert_eq!(0, stun_header.get_marker());
        assert_eq!(0, stun_header.get_m0());
        assert_eq!(0, stun_header.get_m1());
        assert_eq!(1, stun_header.get_m2());
        assert_eq!(56, stun_header.get_length());
        assert_eq!(STUN_MAGIC_COOKIE, stun_header.get_magic_cookie());
        assert_eq!(Method::Binding, stun_header.get_method());
    }
}
