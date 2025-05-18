const mysql = require('mysql2/promise');

async function testConnection() {
  try {
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root', // substitua pelo seu usuário
      password: '', // substitua pela sua senha
      database: 'base_conhecimento_db' // pode usar um banco de dados existente
    });
    
    console.log('Conexão bem-sucedida com o MySQL!');
    const [rows] = await connection.execute('SELECT 1 + 1 AS solution');
    console.log('Resultado do teste:', rows[0].solution);
    
    await connection.end();
  } catch (error) {
    console.error('Erro na conexão:', error);
  }
}

testConnection();

