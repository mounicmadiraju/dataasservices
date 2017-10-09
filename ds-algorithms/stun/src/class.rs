#[derive(Eq, PartialEq, Debug)]
pub enum Class {
    Request,
    Indication,
    Success,
    Error,
}

impl Class {
    pub fn to_u16(self) -> u16 {
        match self {
            Class::Request => 0,
            Class::Indication => 1,
            Class::Success => 2,
            Class::Error => 3
        }
    }

    pub fn from_u16(i: u16) -> Option<Class> {
        match i {
            0 => Some(Class::Request),
            1 => Some(Class::Indication),
            2 => Some(Class::Success),
            3 => Some(Class::Error),
            _ => None
        }
    }
}
