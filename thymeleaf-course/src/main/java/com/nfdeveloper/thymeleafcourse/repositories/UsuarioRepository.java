package com.nfdeveloper.thymeleafcourse.repositories;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import com.nfdeveloper.thymeleafcourse.model.Usuario;

@Repository
@Transactional
public interface UsuarioRepository extends CrudRepository<Usuario, Long>{
 
	@Query("SELECT u from Usuario u WHERE u.login = ?1")
	Usuario findUserByLogin(String login);
	
}
