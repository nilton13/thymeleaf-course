package com.nfdeveloper.thymeleafcourse.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;

@Configuration
@EnableWebSecurity
public class WebConfigSecurity extends WebSecurityConfigurerAdapter{

	@Autowired
	private ImplementacaoUserDetailService usuarioService;
	
	@Override // Configura as solicitações de acesso por HTTP
	protected void configure(HttpSecurity http) throws Exception {
		http.csrf()
			.disable() // Desativa as configurações padrão de memória do Spring
			.authorizeRequests() // Permitir restringir acessos
			.antMatchers(HttpMethod.GET, "/").permitAll() // Qualquer usuário acessa a HOME
			.antMatchers("**/materialize/**").permitAll()
			.antMatchers(HttpMethod.GET, "/cadastropessoa").hasAnyRole("ADMIN") // Só poderá acessar quem tem o usuário ADMIN
			.anyRequest().authenticated()
			.and().formLogin().permitAll() // Permite qualquer usuário ao formulário de login
			.loginPage("/login") // Referenciando Página de Login (login.html)
			.defaultSuccessUrl("/cadastropessoa") // Se o Login funcionar redirecionar para ....
			.failureUrl("/login?error=true") // Se não funcionar redirecionar para...
			.and().logout().logoutSuccessUrl("/login") // Mapeia URL de saida do sistema e invalida o usuario Autenticado
			.logoutRequestMatcher(new AntPathRequestMatcher("/logout"));
	}
	
	@Override // Cria autenticação do usuário com banco de dados em memória
	protected void configure(AuthenticationManagerBuilder auth) throws Exception {
		
		auth.userDetailsService(usuarioService)
			.passwordEncoder(new BCryptPasswordEncoder());
		
		
		/*auth.inMemoryAuthentication().passwordEncoder(new BCryptPasswordEncoder())
			.withUser("nilton")
			.password("123")
			.roles("ADMIN");*/
	}
	
	@Override // Igonra URL específicas
	public void configure(WebSecurity web) throws Exception {
		web.ignoring().antMatchers("/materialize/**")
		.antMatchers(HttpMethod.GET,"/resources/**", "/static/**", "/**", "/materialize/**",
				"**/materialize/**");
	}
}
