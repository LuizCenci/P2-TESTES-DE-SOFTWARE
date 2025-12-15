Feature: Fluxo de navegação e compra no site SauceDemo
  Descrição da funcionalidade:
    Validar que um usuário pode autenticar-se, visualizar produtos,
    acessar detalhes, adicionar ao carrinho e navegar corretamente.

  Papel do usuário:
    Consumidor utilizando a interface web.

  Objetivo de uso:
    Garantir que as funcionalidades essenciais funcionam sem falhas.

  Background:
    Given que o navegador está aberto
    And que estou na página inicial do site SauceDemo

  # -----------------------------
  # CENÁRIO 1 - LOGIN
  # -----------------------------
  Scenario: Usuário realiza login com sucesso
    When informo o usuário "standard_user"
    And informo a senha "secret_sauce"
    And clico no botão de login
    Then devo ver a lista de produtos carregada
    And o título da página deve ser "Products"

  # -----------------------------
  # CENÁRIO 2 - ABRIR DETALHES
  # -----------------------------
  Scenario: Usuário abre detalhes de um produto
    Given que estou logado no sistema
    When clico no produto "Sauce Labs Backpack"
    Then devo ver a página de detalhes desse produto
    And o botão "Add to cart" deve estar visível

  # -----------------------------
  # CENÁRIO 3 - ADICIONAR AO CARRINHO
  # -----------------------------
  Scenario: Usuário adiciona um item ao carrinho
    Given que estou logado no sistema
    When adiciono o produto "Sauce Labs Bike Light" ao carrinho
    Then o ícone do carrinho deve mostrar "1"

  # -----------------------------
  # SCENARIO OUTLINE - LOGIN COM VARIAÇÕES
  # -----------------------------
  Scenario Outline: Tentativas de login com diferentes credenciais
    When informo o usuário "<usuario>"
    And informo a senha "<senha>"
    And clico no botão de login
    Then devo ver "<resultado>"

    Examples:
      | usuario         | senha         | resultado                                      |
      | standard_user   | secret_sauce  | Products                                       |
      | locked_out_user | secret_sauce  | Epic sadface: Sorry, this user has been locked out. |
      | standard_user   | errado        | Epic sadface: Username and password do not match |
