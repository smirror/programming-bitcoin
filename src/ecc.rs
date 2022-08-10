#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct FieldElement {
    num: isize,
    prime:  isize,
}

impl FieldElement{
    pub fn init(num: isize, prime: isize) -> FieldElement {
        // if num >= prime {
        //     panic!("num {} not in field range 0 to {}", num, prime - 1);
        // }
        FieldElement {
            num: num % prime,
            prime
        }
    }

    pub fn add(&self, other: &FieldElement) -> FieldElement {
        FieldElement::init(self.num + other.num, self.prime)
    }

    pub fn sub(&self, other: &FieldElement) -> FieldElement {
        FieldElement::init(self.num - other.num, self.prime)
    }

}

#[cfg(test)]
mod tests{
    use crate::ecc::FieldElement;

    #[test]
    fn test_partial_eq(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a == b, false);
        assert_eq!(a != b,true);
    }

    #[test]
    fn test_eq(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a == a, true);
    }

    #[test]
    fn test_add(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        let c = FieldElement::init(13, 13);
        assert_eq!(a.add(&b), c);
    }

    #[test]
    fn test_sub(){
        let a = FieldElement::init(6, 13);
        let b = FieldElement::init(7, 13);
        let c = FieldElement::init(-1, 13);
        assert_eq!(a.sub(&b), c);
    }
}
