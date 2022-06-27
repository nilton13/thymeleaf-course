package com.nfdeveloper.thymeleafcourse.Controllers;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.nfdeveloper.thymeleafcourse.model.Pessoa;
import com.nfdeveloper.thymeleafcourse.model.Telefone;
import com.nfdeveloper.thymeleafcourse.repositories.PessoaRepository;
import com.nfdeveloper.thymeleafcourse.repositories.TelefoneRepository;

@Controller
public class PessoaController {

    @Autowired
    private PessoaRepository repository;
    @Autowired
    private TelefoneRepository telefoneRepository;
    
    @GetMapping("/cadastropessoa")
    public ModelAndView inicio(){
        ModelAndView modelAndView = new ModelAndView("cadastro/cadastropessoa");
        modelAndView.addObject("pessoaobj", new Pessoa());
        Iterable<Pessoa> pessoasIt = repository.findAll();
        modelAndView.addObject("pessoas", pessoasIt);
        return modelAndView;
    }

    @PostMapping(value="**/salvarpessoa")
    public ModelAndView salvar(Pessoa pessoa){
        repository.save(pessoa);

        ModelAndView andView = new ModelAndView("cadastro/cadastropessoa");
        Iterable<Pessoa> pessoasIt = repository.findAll();
        andView.addObject("pessoas", pessoasIt);
        andView.addObject("pessoaobj", new Pessoa());

        return andView;
    }

    // Enviando todas as pessoas salvas no sistema para a tela.
    @GetMapping("/listapessoas")
    public ModelAndView pessoas(){
        ModelAndView andView = new ModelAndView("cadastro/cadastropessoa");
        Iterable<Pessoa> pessoasIt = repository.findAll();
        andView.addObject("pessoas", pessoasIt);
        andView.addObject("pessoaobj", new Pessoa());
        return andView;
    }

    @GetMapping("/editarpessoa/{idpessoa}")
    public ModelAndView editar(@PathVariable("idpessoa") Long idpessoa){

        Optional<Pessoa> pessoa = repository.findById(idpessoa);
        ModelAndView modelAndView = new ModelAndView("cadastro/cadastropessoa");
        modelAndView.addObject("pessoaobj", pessoa.get());
        return modelAndView;
    }
    
    //Removendo pessoa
    @GetMapping("/removerpessoa/{idpessoa}")
    public ModelAndView excluir(@PathVariable("idpessoa") Long idpessoa){

        repository.deleteById(idpessoa);
    	
        ModelAndView modelAndView = new ModelAndView("cadastro/cadastropessoa");
        modelAndView.addObject("pessoas", repository.findAll());
        modelAndView.addObject("pessoaobj", new Pessoa());
        return modelAndView;
    }
    
    //Pesquisando pessoas pelo Nome
    @PostMapping("**/pesquisarpessoa")
    public ModelAndView pesquisarpessoa(@RequestParam("nomepesquisa") String nomepesquisa) {
    	ModelAndView modelAndView = new ModelAndView("cadastro/cadastropessoa");
    	modelAndView.addObject("pessoas", repository.findPessoaByName(nomepesquisa));
    	modelAndView.addObject("pessoaobj", new Pessoa());
    	return modelAndView;
    }
    
    //Recuperando telefones de pessoas - RELACIONAMENTO
    @GetMapping("/telefones/{idpessoa}")
    public ModelAndView telefones(@PathVariable("idpessoa") Long idpessoa){

        Optional<Pessoa> pessoa = repository.findById(idpessoa);
        
        ModelAndView modelAndView = new ModelAndView("cadastro/telefones");
        modelAndView.addObject("pessoaobj", pessoa.get());
        modelAndView.addObject("telefones", telefoneRepository.getTelefones(idpessoa));
        return modelAndView;
    }
    
    @PostMapping("**/addfonePessoa/{pessoaid}")
    public ModelAndView addFonePessoa(Telefone telefone, @PathVariable("pessoaid") Long pessoaid) {
    	
    	Pessoa pessoa = repository.findById(pessoaid).get();
    	
    	// Validação de Dados do Lado do Servidor
    	/*
    	if(telefone != null && telefone.getNumero().isEmpty() || telefone.getTipo().isEmpty()) {
    		
    		ModelAndView modelAndView = new ModelAndView("cadastro/telefones");  
    		modelAndView.addObject("pessoaobj", pessoa);
    		modelAndView.addObject("telefones", telefoneRepository.getTelefones(pessoaid));
    		List<String> msg = new ArrayList<String>();
    		if(telefone.getNumero().isEmpty()) {
    			msg.add("Número deve ser informado");    			
    		}
    		if(telefone.getTipo().isEmpty()) {
    			msg.add("Tipo do telefone deve ser informado");
    		}
    		modelAndView.addObject("msg", msg);
    		
    		return modelAndView;
    	}*/
    	
    	telefone.setPessoa(pessoa);
    	telefoneRepository.save(telefone);
    	
    	ModelAndView modelAndView = new ModelAndView("cadastro/telefones");  	
    	modelAndView.addObject("pessoaobj", pessoa);
    	modelAndView.addObject("telefones", telefoneRepository.getTelefones(pessoaid));
    	return modelAndView;
    }
    
    @GetMapping("/removertelefone/{idtelefone}")
    public ModelAndView removertelefone(@PathVariable("idtelefone") Long idtelefone){
    	
    	 Pessoa pessoa = telefoneRepository.findById(idtelefone).get().getPessoa();

        telefoneRepository.deleteById(idtelefone);
    	
        ModelAndView modelAndView = new ModelAndView("cadastro/telefones");
        modelAndView.addObject("pessoaobj", pessoa);
        modelAndView.addObject("telefones", telefoneRepository.getTelefones(pessoa.getId()));
        return modelAndView;
    }
}
