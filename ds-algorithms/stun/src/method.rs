#[derive(Eq, PartialEq, Debug)]
pub enum Method {
    Binding,
    Allocate,
    Refresh,
    Send,
    Data,
    CreatePerm,
    ChannelBind,
    Other(u16),
}

impl Method {
    pub fn to_u16(self) -> u16 {
        match self {
            Method::Binding => 1,
            Method::Allocate => 3,
            Method::Refresh => 4,
            Method::Send => 5,
            Method::Data => 6,
            Method::CreatePerm => 7,
            Method::ChannelBind => 8,
            Method::Other(i) => i,
        }
    }

    pub fn from_u16(i: u16) -> Option<Method> {
        match i {
            1 => Some(Method::Binding),
            3 => Some(Method::Allocate),
            4 => Some(Method::Refresh),
            5 => Some(Method::Send),
            6 => Some(Method::Data),
            7 => Some(Method::CreatePerm),
            8 => Some(Method::ChannelBind),
            _ => None
        }
    }
}
