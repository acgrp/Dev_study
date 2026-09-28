package hello.servlet.domain.member;

import org.junit.jupiter.api.AfterEach;
import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.Test;

import java.util.List;

class MemberRepositoryTest {

    MemberRepository memberRepository = MemberRepository.getInstance();

    @AfterEach
    void afterEach(){
        memberRepository.clearStore();
    }

    @Test
    void getInstance() {

    }

    @Test
    void save() {
        Member member = new Member("hello", 20);

        Member savedMember = memberRepository.save(member);

        Member findMember = memberRepository.findById(savedMember.getId());
        org.assertj.core.api.Assertions.assertThat(findMember).isEqualTo(savedMember);
    }

    @Test
    void findAll() {
        Member member1 = new Member("member1", 20);
        Member member2 = new Member("member2", 30);

        memberRepository.save(member1);
        memberRepository.save(member2);

        List<Member> result = memberRepository.findAll();

        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(member1, member2);
    }

    @Test
    void clearStore() {

    }
}