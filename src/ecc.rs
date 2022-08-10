#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct FieldElement {
    num: u32,
    prime: u32
}

impl FieldElement{
    pub fn init(num: u32, prime: u32) -> FieldElement {
        if num >= prime {
            panic!("num {} not in field range 0 to {}", num, prime - 1);
        }
        FieldElement {
            num: num % prime,
            prime
        }
    }
}

#[cfg(test)]

mod tests{
    use crate::ecc::FieldElement;

    #[test]
    fn test_partial_eq(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a, a);
        assert_eq!(a == b, false);
        assert_eq!(a == a, true);
    }
}
